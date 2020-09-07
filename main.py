from flask import Flask, render_template
from flask_socketio import SocketIO
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('event to server')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    time.sleep(5)
    # Only send message back to original client
    client_id = json['id']
    socketio.emit('event to client', 
        {'data': json['data'] + 1, 'id': client_id},
        room=client_id)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)


