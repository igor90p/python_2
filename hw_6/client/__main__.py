import json
import hashlib
import socket
from datetime import datetime


socket = socket.socket()
socket.connect(('localhost', 8000))

action = input('Enter action: ')
data = input('Data: ')

hash_obj = hashlib.sha1()
hash_obj.update(b'secret_key')

request_string = json.dumps(
    {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data,
        'user': hash_obj.hexdigest()
    }
)

print(hash_obj.hexdigest())

socket.send(request_string.encode())
while True:
    response = socket.recv(1024)

    if response:

        print(
            response.decode()
        )