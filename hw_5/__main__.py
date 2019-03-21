import json
import socket
import logging
from datetime import datetime

from protocol import (
    validate_request, make_response, 
    make_400, make_404
)
from routes import resolve


logger = logging.getLogger('default')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('default.log')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

sock = socket.socket()
sock.bind(('', 8888))
sock.listen(5)

try:
    while True:
        client, address = sock.accept()
        logger.debug(f'Client detected {address}')
        data = client.recv(1024)
        request = json.loads(data.decode('utf-8'))

        if validate_request(request):
            controller = resolve(request.get('action'))
            if controller:
                try:
                    response = controller(request)
                except Exception:
                    response = make_response(
                        request, 500, 
                        'Internal server error.'
                    )
            else:
                response = make_404(request)
        else:
            response = make_400(request)
    
        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))
        client.close()

except KeyboardInterrupt:
    sock.close()