import json
import hashlib
import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', type=str, default='w')
cmd_args = parser.parse_args()

try:
    sock = socket.socket()
    sock.connect(('localhost', 8888))

    if cmd_args.mode == 'w':

        while True:


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

    else:
        while True:
            response = sock.recv(1024)

            if response:

                print(response.decode())

                break
except KeyboardInterrupt:
    sock.close()
