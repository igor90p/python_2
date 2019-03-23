import json
import socket
import logging
import select
from datetime import datetime

from protocol import (
    validate_request, make_response, 
    make_400, make_404
)
from routes import resolve
from handelers import handle_client_request
from settings import (
    HOST, PORT
)

error_handler = logging.FileHandler('error.log') 
error_handler.setLevel(logging.CRITICAL)

responses = []
connections = []

try:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            error_handler
        ]
    )

    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    logging.info(f'Server start with host:{ HOST } and port: { PORT }')
    while True:
        client, address = sock.accept()
        connections.append(client)
        logging.info(f'Client detected {address}')

        rlist,wlist, xlist = select.select(connections, connections, [], 0)

        for client in connections:

            if client in rlist:
                data = client.recv(1024)
                request = json.loads(data.decode('utf-8'))

                response = handle_client_request(request)

                action_name = request.get('action')

                if response.get('code') == 400:
                    logging.error(f'Bad Request: { action_name } request: { request }')

                if response.get('code') == 200:
                    responses.append(response)

                response_string = json.dumps(response)
                client.send(response_string.encode('utf-8'))

            if client in wlist:
                logging.info(
                    f'Response { responses } sended to {client.getsockname()}'
                )
                if responses:
                    for conn in connections:
                        response_obj_string = json.dumps(responses)
                        conn.send(response_obj_string.encode('utf-8'))

except KeyboardInterrupt:
    logging.info('Shutdown server')
    sock.close()