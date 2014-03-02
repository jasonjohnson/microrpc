from microrpc.decorators import rpc
from microrpc.server import create_server

@rpc
def add_two(a, b):
    return a + b

server = create_server()
server.serve_forever()

