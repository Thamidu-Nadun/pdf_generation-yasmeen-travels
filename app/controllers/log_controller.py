from app.services.log_service import save_log, get_logs

def log_request(request):
    log_data = {
        'user': request.get('user', 'system'),
        'log_type': request.get('log_type', 'info'),
        'status': request.get('status', 'success'),
    }
    return save_log(**log_data)

def retrieve_logs():
    return get_logs()