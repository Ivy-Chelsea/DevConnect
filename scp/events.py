from scp import socketio
from flask import session
from flask_socketio import leave_room, join_room, send
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
    send({
        "sender": "",
        "message": f"{name} has entered the chat"
    }, to=room)
    rooms[room]["members"] += 1


@socketio.on('message')
def handle_message(payload):
    room = session.get('room')
    name = session.get('name')
    if room not in rooms:
        return
    message = {
        "sender": name,
        "message": payload["message"]
    }
    send(message, to=room)
    rooms[room]["messages"].append(message)


@socketio.on('disconnect')
def handle_disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
        send({
        "message": f"{name} has left the chat",
        "sender": ""
    }, to=room)
