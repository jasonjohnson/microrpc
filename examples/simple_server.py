from microrpc import Server

server = Server()

@server.rpc
def add_two(a, b):
    return a + b

server.run()

