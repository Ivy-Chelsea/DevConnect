from scp import socketio
@socketio.on('connect')
def handle_connect():