import os
import time, datetime
from dotenv import load_dotenv
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from . import filters
from playwright.sync_api import sync_playwright
from email_parser.EmailContent import EmailContent
from email_parser import extract_email_data

load_dotenv()

PDF_OUT_DIR = os.path.join(os.getenv("PDF_OUT_DIR"), time.strftime("%Y"), 
                           time.strftime("%m"), time.strftime("%d"))

def render_template(html_template, data):
    template_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    env.filters['comma'] = filters.comma_format
    template = env.get_template(html_template)
    
    return template.render(data)

def generate_pdf(output_path, email_body=""):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        parsed_email_content = None
        parsed_email_content = extract_email_data(email_content=email_body)
        start_date = datetime.datetime.strptime(parsed_email_content.start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(parsed_email_content.end_date, "%Y-%m-%d")
        
        issue_number = str(start_date.year) + " / " + start_date.strftime("%m%d") + "-" + end_date.strftime("%m%d")
        generated_date = datetime.datetime.now().strftime("%Y / %m%d")
        
        content_injected = {
            "name": parsed_email_content.customer_name,
            "issue_number": issue_number,
            "generated_date": generated_date,
            "month": start_date.strftime("%b"),
            "passenger_count": parsed_email_content.total_pax,
            "operator": parsed_email_content.operator_name,
            "plans": '<br/>'.join(parsed_email_content.iternary),
            "remarks": [
                "some remarks",
                "some more remarks"
            ],
            "vehicle_type": parsed_email_content.vehicle_type,
            "staff_assignment": parsed_email_content.staff_assignment,
            "total_fee": "100000"
        }
        
        print("Content to be injected: ", content_injected['plans'])
        parsed_email_content = None
        
        content = render_template("template_confirmation.html", content_injected)
        page.set_content(content)
        page.pdf(path=output_path, 
                 format='A4', 
                 print_background=True, 
                 display_header_footer=False)
        browser.close()


def save_pdf(to_email: str, email_body: str) -> str:
    """Generate PDF and save it in storage

    Args:
        to_email (string): email address of the recipient
        email_body (TEXT): email body content to be included in the PDF

    Returns:
        string: path to the saved PDF file
    """
    output_path = os.path.join(PDF_OUT_DIR, f"{to_email}.pdf")
    if not os.path.exists(PDF_OUT_DIR):
        os.makedirs(PDF_OUT_DIR)
        
    print(f"Generating PDF at: {output_path}")
    generate_pdf(output_path, email_body)
    print(f"PDF generated and saved at: {output_path}")
    return output_path

if __name__ == "__main__":
    to_email = "test@gmail.com"
    email_body = "This is a test email body."
    pdf_path = save_pdf(to_email, email_body)
    print(f"PDF saved at: {pdf_path}")
