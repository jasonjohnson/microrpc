from microrpc.server import create_server

server = create_server()

@server.rpc
def add_two(a, b):
    return a + b

server.serve_forever()

