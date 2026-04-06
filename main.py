from flask import Flask, request, jsonify
from pdf_generation import save_pdf
from email_sender import send_email_with_attachment

app = Flask(__name__)

@app.route('/')
def index():
    return "Email Sender App is running!"

@app.route('/save_email', methods=['POST'])
def save_email():
    data = request.get_json()
    to_email = data.get('to_email')
    subject = data.get('subject')
    body = data.get('body')
    
    response = {
        "status_code": 201,
        "message": "Email data received and saved successfully.",
        "data": {
            "to_email": to_email,
            "subject": subject,
            "body": body
        }
    }
    print(f"Received email data: To: {to_email}, Subject: {subject}, Body: {body}")
    
    # todo: save_pdf(body) -> path
    saved_path = save_pdf(to_email, body)
    
    # todo temp: save_email(to_email, subject, body, pdf_path)
    # only for testing i'll send the mail once it confirm in send_mail() function
    # send_email_with_attachment(to_email, subject, body, saved_path)
    
    return jsonify(response), 201

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    email_id = data.get('email_id')
    
    # todo: email_data = get_email_data(email_id)
    # todo: send_email(to_email, subject, body, pdf_path) -> 1/0

@app.errorhandler(404)
def not_found():
    return jsonify({
        "status_code": 404,
        "message": "The requested resource was not found."
    }), 404
    

if __name__ == '__main__':
    app.run()