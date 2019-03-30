import json
import logging
from routes import resolve

from protocol import (
    validate_request, make_response,
    make_400, make_404
)

def read_request(client, requests):
    data = client.recv(1024)

    if data:
        request = json.loads(data.decode('utf-8'))
        requests.append(request)

def write_response(client, request):
    response = None
    action_name = request.get('action')
    
    if validate_request(request):
        controller = resolve(action_name)
        if controller:
            try:
                response = controller(request)
            except Exception as err:
                logging.critical(err, exc_info=True)
                response = make_response(
                    request, 500,
                    'Internal server error.'
                )
        else:
            logging.error(f'Action not found: { action_name }')
            response = make_404(request)
    else:
        logging.error(f'Bad Request: { action_name } request: { request }')
        response = make_400(request)

    response_string = json.dumps(response)
    client.send(response_string.encode('utf-8'))