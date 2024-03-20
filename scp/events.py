from scp import socketio
@socketio.on('connect')
def handle_connect():
    name = session.get('name')
    room = session.get('room')