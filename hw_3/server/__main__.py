import json
import socket
from datetime import datetime

sock = socket.socket()
sock.bind(('', 7777))
sock.listen(5)

while True:
    client, address = sock.accept()
    print(f'Client detected {address}')
    data = client.recv(1024)
    request = json.loads(data.decode('utf-8'))
    
    if request.get('action') == 'get_time':
        date = datetime.now()
        response_string = date.strftime('%d-%m-%yT%H:%M:%S')

    elif request.get('action') == 'upper_text':
        client_data = request.get('data')
        response_string = client_data.upper()

    client.send(response_string.encode('utf-8'))
    client.close()
    

