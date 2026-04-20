from app.extensions import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pdf_path = db.Column(db.String(255), nullable=True)
    