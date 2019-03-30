import json
import socket
import select
import logging
import threading
import collections
from datetime import datetime

from protocol import (
    validate_request, make_response, 
    make_400, make_404
)
from routes import resolve
from utils import get_client_fullname
from handelers import write_response, read_request
from settings import (
    HOST, PORT
)


error_handler = logging.FileHandler('error.log') 
error_handler.setLevel(logging.CRITICAL)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        error_handler
    ]
)

requests = collections.deque()
connections = []

try:
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    sock.settimeout(0)

    logging.info(f'Server start with host:{ HOST } and port: { PORT }')

    while True:
        try:
            client, address = sock.accept()
            connections.append(client)
            logging.info(f'Client detected { "%s:%s" % address }')
        except OSError:
            pass

        rlist, wlist, xlist = select.select(
            connections, connections, [], 0
        )

        for client in rlist:
            target = read_thread = threading.Thread(read_request, args=(client, requests))
            read_thread.start()
    
        if requests:
            requests = requests.popleft()
            for client in wlist:
                target = write_thread = threading.Thread(write_response, args=(client, request))
                write_thread.start()
                logging.info(
                    f'Request { request } handled and sended to {client.getsockname()}'
                )

except KeyboardInterrupt:
    logging.info('Shutdown server')
    sock.close()