import pathlib
from flask import Flask, request, jsonify
from pdf_generation import save_pdf
from email_sender import send_email_with_attachment
from repo.init_db import init_db, get_db_connection
from repo.Email import Email, EmailRepo
from models.Response import Response

app = Flask(__name__)

if (init_db()):
    print("Database initialized successfully.")
else:
    print("Database initialization failed.")


@app.route('/')
def index():
    return "Email Sender App is running!"

@app.route('/save_email', methods=['POST'])
def save_email():
    data = request.get_json()
    to_email = data.get('to_email')
    subject = data.get('subject')
    body = data.get('body')
    
    print(f"Received email data: To: {to_email}, Subject: {subject}, Body: {body}")
    
    try: 
        saved_path = save_pdf(to_email, body)
        abs_saved_path = str(pathlib.Path(saved_path).absolute())
        
        email = Email(
            receipient=to_email,
            subject=subject,
            body=body,
            pdf_path=abs_saved_path
        )
        with get_db_connection() as conn:
            email_repo = EmailRepo(conn)
            email_repo.save_email(email)
        
        
        response = Response(201, "Email data saved successfully.").to_dict()
        return jsonify(response), 201
    except Exception as e:
        print(f"Error saving email data: {e}")
        response = Response(500, "An error occurred while saving email data.").to_dict()
        return jsonify(response), 500

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    email_id = data.get('email_id')
    
    with get_db_connection() as conn:
        email_repo = EmailRepo(conn)
        email_data = email_repo.get_email_data(email_id=email_id)
        
        if email_data:
            if send_email_with_attachment(to_email=email_data.receipient,
                                          subject=email_data.subject,
                                          body=email_data.body,
                                          attachment_path=email_data.pdf_path):
                response = Response(200, "Email sent successfully.", email_data.to_dict()).to_dict()
                return jsonify(response), 200
        else:
            response = Response(404, f"No email found with ID {email_id}.").to_dict()
            return jsonify(response), 404

@app.errorhandler(404)
def not_found():
    return jsonify({
        "status_code": 404,
        "message": "The requested resource was not found."
    }), 404
    

if __name__ == '__main__':
    app.run()