from scp import socketio
from flask import session


@socketio.on('connect')
def handle_connect():
    name = session.get('name')
    room = session.get('room')
    if name is None or room is None:
        return