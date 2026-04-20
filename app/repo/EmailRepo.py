from app.extensions import db
from app.models.Email import Email

def create_email(receipient, subject, body, pdf_path):
    """Create a new email record in the database.
    Args:
        receipient (str): The email recipient.
        subject (str): The email subject.
        body (str): The email body.
        pdf_path (str): The file path to the generated PDF.
    Returns:
        Email: The created Email object.
    """
    new_email = Email(
        receipient=receipient,
        subject=subject,
        body=body,
        pdf_path=pdf_path
    )
    db.session.add(new_email)
    db.session.commit()
    return new_email

def get_email_by_id(email_id):
    """Retrieve an email record by its ID.
    Args:
        email_id (int): The ID of the email to retrieve.
    Returns:
        Email: The Email object with the specified ID, or None if not found.
    """
    return Email.query.get(email_id)

def get_email_by_receipient(receipient):
    """Retrieve email records by recipient email address.
    Args:
        receipient (str): The email recipient to search for.
    Returns:
        list: A list of Email objects that match the specified recipient.
    """
    return Email.query.filter_by(receipient=receipient).all()

def get_all_emails():
    """Retrieve all email records from the database.
    Returns:
        list: A list of all Email objects in the database.
    """
    return Email.query.all()

def delete_email(email_id):
    """Delete an email record by its ID.
    Args:
        email_id (int): The ID of the email to delete.
    Returns:
        bool: True if the email was deleted, False if not found.
    """
    email = Email.query.get(email_id)
    if email:
        db.session.delete(email)
        db.session.commit()
        return True
    return False