from scp import socketio
from flask import session
from flask_socketio import leave_room, join_room
from scp.data import rooms


@socketio.on('connect')
def handle_connect():
    name = session.get('name')
    room = session.get('room')
    if name is None or room is None:
        return
    if room not in rooms:
        leave_room(room)
    join_room(room)
