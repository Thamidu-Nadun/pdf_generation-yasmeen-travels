from email_parser.EmailContent import EmailContent

class Email:
    def __init__(self, receipient: str, subject: str, body: EmailContent, pdf_path: str):
        self.receipient = receipient
        self.body = body
        self.subject = subject
        self.pdf_path = pdf_path

    def to_dict(self):
        return {
            "receipient": self.receipient,
            "subject": self.subject,
            "body": self.body,
            "pdf_path": self.pdf_path
        }
        
class EmailRepo:
    def __init__(self, conn):
        self.conn = conn
        
    def save_email(self, email: Email):
        self.conn.execute('''
                          INSERT INTO emails (receipient, subject, body, pdf_path) 
                          VALUES (?, ?, ?, ?)
                          ''', 
                          (email.receipient, email.subject, email.body, email.pdf_path))
        self.conn.commit()
        
    def get_email_data(self, email_id: int) -> Email:
        cur = self.conn.execute('''SELECT receipient, subject, body, pdf_path 
                                FROM emails
                                WHERE id = ?''', (email_id,))
                          
        row = cur.fetchone()
        if row:
            return Email(receipient=row[0], subject=row[1], body=row[2], pdf_path=row[3])
        else:
            return None

    