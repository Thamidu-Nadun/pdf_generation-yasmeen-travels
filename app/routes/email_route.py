from flask import Blueprint, request, jsonify

email_bp = Blueprint('email', __name__)

@email_bp.route('/', methods=['POST'])
def save_email():
    data = request.get_json()
    if not data or 'to_email' not in data or 'body' not in data:
        return jsonify({"error": "Missing 'to_email' or 'body' in request"}), 400
    
    mail_type = data.get('mail_type', 'confirmation')
    to_email = data['to_email']
    subject = data['subject']
    email_body = data['body']
    
    # Call the service layer to save the email
    
@email_bp.route('/<int:email_id>', methods=['GET'])
def get_email(email_id):
    pass