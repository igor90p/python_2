import json
import socket


socket = socket.socket()
socket.connect(('localhost', 7777))

action = input('Enter action: ')
data = input('Data: ')

request_string = json.dumps(
    {
        'action': action,
        'data': data
    }
)

socket.send(request_string.encode())
while True:
    response = socket.recv(1024)
    if response:

        print(response.decode())

        socket.close()

        break