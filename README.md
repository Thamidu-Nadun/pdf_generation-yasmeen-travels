# Email Agent - PDF Generation & Distribution

A Flask-based application that intelligently parses email content, generates professional PDF documents, and manages email distribution with attachments. Built to automate email processing workflows with support for dynamic PDF rendering and database persistence.

## 🎯 Features

- **Email Parsing**: Intelligently extract structured data from raw email content using regex-based parsing
- **PDF Generation**: Dynamically generate professional PDFs from email data using Playwright and Jinja2 templates
- **Email Sending**: Send emails with PDF attachments automatically
- **Data Persistence**: Store email records and PDF paths in a SQLite database
- **Template Support**: Flexible Jinja2 HTML templates for PDF rendering with custom filters
- **RESTful API**: Simple Flask endpoints for email submission and processing

## 🛠️ Tech Stack

- **Backend**: Python 3.x with Flask
- **PDF Generation**: Playwright (Chromium), Jinja2
- **Database**: SQLite
- **Email**: Python email libraries
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd pdf_generation
   ```

2. **Create and activate virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:

   ```
   PDF_OUT_DIR=./pdf
   DATABASE_PATH=/db/pdf_generation.db
   ```

5. **Initialize the database**
   ```bash
   python -c "from repo.init_db import init_db; init_db()"
   ```

## 🚀 Usage

### Starting the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

### API Endpoints

#### POST `/save_email`

Save and process an email with PDF generation.

**Request Body:**

```json
{
  "to_email": "recipient@example.com",
  "subject": "Email Subject",
  "body": "Customer Name: John Doe\nStart Date: 2026-01-01\nEnd Date: 2026-03-31\n[Items]\nItem 1: $100\nItem 2: $200"
}
```

**Response:**

```json
{
  "status_code": 201,
  "message": "Email data saved successfully.",
  "data": {
    "id": 1,
    "recipient": "recipient@example.com",
    "subject": "Email Subject",
    "pdf_path": "/path/to/pdf/2026/03/28/email_id_1.pdf"
  }
}
```

#### GET `/`

Health check endpoint that returns a simple status message.

## 📁 Project Structure

```
pdf_generation/
├── main.py                      # Flask application entry point
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (create this)
├── README.md                   # This file
│
├── email_parser/               # Email parsing module
│   ├── __init__.py
│   ├── app.py                 # Parsing functions
│   ├── EmailContent.py        # EmailContent data model
│   └── mail2.txt              # Sample email data
│
├── email_sender/               # Email sending module
│   ├── __init__.py
│   └── app.py                 # Email sending functions
│
├── pdf_generation/             # PDF generation module
│   ├── __init__.py
│   ├── app.py                 # PDF generation functions
│   ├── filters.py             # Jinja2 custom filters
│   ├── req-format.json        # Format configuration
│   ├── static/                # Static assets
│   └── templates/             # HTML templates
│       ├── confirmation.html
│       └── template_confirmation.html
│
├── models/                     # Data models
│   └── Response.py            # Response wrapper class
│
├── repo/                       # Database layer
│   ├── Email.py               # Email model and repository
│   └── init_db.py             # Database initialization
│
├── pdf/                        # Generated PDFs (organized by date)
│   └── YYYY/MM/DD/            # Date-based directory structure
│
└── temp/                       # Temporary files
```

## 📊 Data Models

### EmailContent

Represents parsed email data with fields like:

- `customer_name`: Name of the customer
- `start_date`: Period start date
- `end_date`: Period end date
- Line items and amounts

### Email

Database model for storing email records:

- `recipient`: Email address
- `subject`: Email subject
- `body`: Parsed email content
- `pdf_path`: Path to generated PDF

## 🔧 Configuration

### Environment Variables

| Variable        | Description                         | Default                 |
| --------------- | ----------------------------------- | ----------------------- |
| `PDF_OUT_DIR`   | Output directory for generated PDFs | `./pdf`                 |
| `DATABASE_PATH` | SQLite database file location       | `/db/pdf_generation.db` |

### Custom Jinja2 Filters

The `filters.py` module contains custom template filters for PDF rendering:

- `comma`: Format numbers with comma separators

## 📝 Email Format

The email parser expects email bodies in a structured format:

```
Customer Name: John Doe
Start Date: 2026-01-01
End Date: 2026-03-31
Invoice Total: $1,500.00
[Items]
Service A: $800.00
Service B: $700.00
```

Ensure emails follow this format for accurate parsing.

## 🗂️ PDF Organization

Generated PDFs are automatically organized by date in the following structure:

```
pdf/
  2026/
    03/
      28/
        email_1.pdf
        email_2.pdf
      29/
        email_3.pdf
    04/
      01/
        email_4.pdf
```

## 💾 Database

The application uses SQLite for data persistence. The database is automatically initialized on first run, creating the necessary tables for storing email records and metadata.

## 🐛 Troubleshooting

**PDF generation fails**: Ensure Playwright chromium is properly installed. Run `playwright install chromium`.

**Database initialization error**: Check that the database directory exists and you have write permissions.

**Email parsing issues**: Verify email content follows the expected format described above.

## 📄 License

[Add your license information here]

## 👥 Contributing

[Add contribution guidelines here]

## 📧 Support

For issues or questions, please contact the development team.
