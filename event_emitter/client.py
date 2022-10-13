import socketio
import json
import amqp
import os

broker="20.218.71.141"  # e-mail might list a different ip
user="b1e7e6eb"
password="5e49afa6d1c4a77704974e2c33beb2fc"
queue=user  # The queue name is set to be the same as the user ID

SERVER_CONNECTION = os.getenv("SERVER_CONNECTION")


print(SERVER_CONNECTION)


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
 
sio.connect(f'http://127.0.0.1:4000')
