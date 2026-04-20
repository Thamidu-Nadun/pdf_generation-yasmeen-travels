import datetime
from app.repo.LogRepo import create_log, get_all_logs

def save_log(user: str, log_type: str, status: bool) -> dict:
    """
    Logs the details of an action performed by a user.
    
    Args:
        user (str): The username of the user performing the action.
        log_type (str): The type of action being logged (e.g: pdf_generation, email_send, email_parser).
        status (bool): The status of the action.
        
    Returns:
        dict: A dictionary containing the log details.
        
    """
    timestamp = datetime.datetime.now()
    return create_log(user, log_type, timestamp, status)

def get_logs() -> list[dict]:
    """
    Retrieves all logs from the database.
    
    Returns:
        list: A list of log records.
    """
    return get_all_logs()