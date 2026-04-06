import json

class EmailContent:
    def __init__(self, customer_name: str = None, start_date = "YY/MM/DD", end_date="YY/MM/DD",
                 total_pax: int = 0, operator_name: str = None,
                 vehicle_type: str = None,
                 staff_assignment: dict = None,
                 iternary: list = None,
                 total_fee: int = 0):
        self.customer_name = customer_name
        self.start_date = start_date
        self.end_date = end_date
        self.total_pax = total_pax
        self.operator_name = operator_name
        self.vehicle_type = vehicle_type
        self.staff_assignment = staff_assignment if staff_assignment is not None else {}
        self.iternary = iternary if iternary is not None else []
        self.total_fee = total_fee
        
    def __str__(self):
        return json.dumps({
            "customer_name": self.customer_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_pax": self.total_pax,
            "operator_name": self.operator_name,
            "vehicle_type": self.vehicle_type,
            "staff_assignment": self.staff_assignment,
            "iternary": self.iternary,
            "total_fee": self.total_fee
        }, indent=4)

class Email:
    def __init__(self, to_email: str, subject: str, email_content: EmailContent):
        self.to_email = to_email
        self.subject = subject
        self.email_content = email_content
        
    def __str__(self):
        _email_content = json.loads(str(self.email_content))
        return json.dumps({
            "to_email": self.to_email,
            "subject": self.subject,
            "email_content": _email_content
        }, indent=4)