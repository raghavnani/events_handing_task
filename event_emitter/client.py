import socketio
import json
import amqp
import os

SERVER_CONNECTION = os.getenv("SERVER_CONNECTION")

broker = os.getenv("BROKER")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
queue = user


sio = socketio.Client()



@sio.event
def connect():
    print('connection established')

    with amqp.Connection(broker, userid=user, password=password) as c:
                ch = c.channel()
                def on_message(message):
                    
                    msg = json.loads(message.body)

                    if msg["resource"] == "building":
                        sio.emit('building', {'response': msg})

                    if msg["resource"] == "room":
                        sio.emit('room', {'response': msg})

                    #exit(0)  # Exit after the first message, to not drain the queue needlessly
                    
                ch.basic_consume(queue, callback=on_message)
                while True:
                    c.drain_events()


@sio.event
def disconnect():
    print('disconnected from server')
 
sio.connect('http://localhost:4000')
