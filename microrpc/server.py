import pickle
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

class Handler(BaseRequestHandler):
    def handle(self):
        while True:
            buff = bytearray()

            while not buff.endswith(b'.'):
                buff += self.request.recv(256)

            method, args, kwargs = pickle.loads(buff)

            try:
                result = self.server.methods[method](*args, **kwargs)
            except Exception as e:
                result = e

            self.request.sendall(pickle.dumps(result))

class Server(ThreadingMixIn, TCPServer):
    def __init__(self, host, port, handler):
        super().__init__((host, port), handler)
        self.methods = {}

    def rpc(self, func):
        self.methods[func.__name__] = func
        return func

def create_server(host='0.0.0.0', port=9090):
    return Server(host, port, Handler)

