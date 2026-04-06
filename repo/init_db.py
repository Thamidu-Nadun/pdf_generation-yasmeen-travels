import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / 'db' / 'pdf_generation.db'

SCHEMA = '''
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receipient TEXT NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    pdf_path TEXT NOT NULL
);
'''


def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Init the database connection with tables.
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        with get_db_connection() as conn:
            conn.executescript(SCHEMA)
            print("Database initialized successfully.")
            return True, "Database initialized successfully."
    except Exception as e:
        return False, f"Database initialization failed: {str(e)}"
