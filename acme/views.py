from flask import Blueprint, request, jsonify
from .models import create_event, get_events, get_event, update_event, delete_event

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/', methods=['POST'])
def add_event():
    data = request.data.decode('utf-8').split('|')
    if len(data) != 3:
        return "Invalid data format", 400

    date, title, text = data
    try:
        event_id = create_event(date, title, text)
        return jsonify({"id": event_id}), 201
    except Exception as e:
        return str(e), 400

@calendar_bp.route('/', methods=['GET'])
def list_events():
    events = get_events()
    return jsonify([{"id": e[0], "date": e[1], "title": e[2], "text": e[3]} for e in events])

@calendar_bp.route('/<int:event_id>/', methods=['GET'])
def read_event(event_id):
    event = get_event(event_id)
    if event:
        return jsonify({"id": event[0], "date": event[1], "title": event[2], "text": event[3]})
    return "Event not found", 404

@calendar_bp.route('/<int:event_id>/', methods=['PUT'])
def update_event_data(event_id):
    data = request.data.decode('utf-8').split('|')
    if len(data) != 2:
        return "Invalid data format", 400

    title, text = data
    updated = update_event(event_id, title, text)
    if updated:
        return "updated", 200
    return "Event not found", 404

@calendar_bp.route('/<int:event_id>/', methods=['DELETE'])
def delete_event_data(event_id):
    deleted = delete_event(event_id)
    if deleted:
        return "deleted", 200
    return "Event not found", 404

@calendar_bp.route('/favicon.ico')
def favicon():
    return '', 204


