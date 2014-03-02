from microrpc.server import METHODS

def rpc(func):
    METHODS[func.__name__] = func
    return func

