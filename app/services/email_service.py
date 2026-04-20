from app.utils.email_parser import extract_email_data
from app.repo.EmailRepo import create_email, get_email_by_id, get_all_emails, get_email_by_receipient, delete_email


def save_email(to_email, subject, body, mail_type='confirmation'):
    # 1. extract email data
    # 2. generate PDF: path
    # 3. save email record to database
    # 4. log it.
    pass

def get_email(email_id):
    return get_email_by_id(email_id)

def get_emails_by_receipient(receipient):
    return get_email_by_receipient(receipient)

def get_emails():
    return get_all_emails()