import pickle
import socket

class Client(object):
    def __init__(self, host='0.0.0.0', port=9090):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def __getattr__(self, method):
        def invoke(*args, **kwargs):
            self.socket.sendall(pickle.dumps((method, args, kwargs)))
            buff = bytearray()

            while not buff.endswith(b'.'):
                buff += self.socket.recv(256)

            result = pickle.loads(buff)

            if isinstance(result, Exception):
                raise result
            return result
        return invoke

    def __del__(self):
        self.socket.close()

