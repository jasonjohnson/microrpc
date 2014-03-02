import pickle
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

METHODS = {}

class Handler(BaseRequestHandler):
    def handle(self):
        while True:
            buff = bytearray()

            while not buff.endswith(b'.'):
                buff += self.request.recv(256)

            method, args, kwargs = pickle.loads(buff)

            try:
                result = METHODS[method](*args, **kwargs)
            except Exception as e:
                result = e

            self.request.sendall(pickle.dumps(result))

class Server(ThreadingMixIn, TCPServer):
    pass

def create_server(host='0.0.0.0', port=9090):
    return Server((host, port), Handler)

