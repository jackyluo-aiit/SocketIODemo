from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from utils import args_verification, statusVo, resultVo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iems5722'
socketio = SocketIO(app)


@app.route("/api/a4/broadcast_room", methods=["GET", "POST"])
def broadcast_room():
    message = request.get_json(force=True)
    if args_verification(message):
        print(message)
        socketio.emit('room_message', {'message': message}, room=message['chatroom_id'])
        return statusVo(message="Broadcast successfully.", status="OK")
    else:
        return statusVo(message="Broadcast failed.", status="ERROR")


@socketio.on('my event')
def my_event_handler(data):
    emit('my event', data, broadcast=True)


@socketio.on('join')
def on_join(data):
    room = data['chatroom_id']
    join_room(room)
    emit('status', 'Entered the room ' + room)


@socketio.on('leave')
def on_leave(data):
    room = data['chatroom_id']
    leave_room(room)
    emit('status', 'Left the room ' + room)


@socketio.on('text')
def update_handler(json):
    emit('update', {'text': json['text']}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001, debug=True)
