from flask import Blueprint, request, jsonify
from app.controllers.log_controller import log_request, retrieve_logs

log_bp = Blueprint('log', __name__)

@log_bp.route('/', methods=['GET'])
def get_logs():
    logs = retrieve_logs()
    return jsonify([log.to_dict() for log in logs]), 200

@log_bp.route('/', methods=['POST'])
def create_log():
    log_data = request.json
    if not log_data:
        return jsonify({'error': 'No log data provided'}), 400
    
    log_entry = log_request(log_data)
    return jsonify(log_entry.to_dict()), 201