microrpc
========

A micro framework for creating RPC clients and servers in Python.

Usage
-----

First, we need to build our RPC server. To begin we will built a function to multiply two things.

```py
def multiply(a, b):
    return a * b
```

To enable RPC for this function, we simple create a server and decorate our function. Once decorated, we can start the server and wait for our first call.

```py
from microrpc.server import create_server

server = create_server()

@server.rpc
def multiply(a, b):
    return a * b

server.serve_forever()
```

Now we need a client to call our function.

```py
from microrpc.client import create_client

client = create_client()
print(client.multiply(2, 10))
```

Most existing functions can be handled this way. Any exceptions raised server-side will be raised client side if possible. Critical errors will of course do horrible things to your server. Any parameter or return type supported by **pickle** may be used.


Installing
----------

```
$ pip install microrpc
```

Installing From Source
----------------------

First, we'll need Python 3. There's no reason this couldn't support Python 2.7, but I wanted to get the proof of concept published first.

```
$ apt-get install python3.3
```

On Ubuntu there's a known incompatibility with Python 3 and the packaged virtualenv, so get a newer version from pypi.

```
$ pip install virtualenv
$ virtualenv --version
1.11.4
```

Get the code and establish a virtualenv.

```
$ git clone git@github.com:jasonjohnson/microrpc.git
$ cd microrpc
$ virtualenv -p /usr/bin/python3.3 env
$ source env/bin/activate
(env) $
```

Now we can install the package and run the example server and client.

```
(env) $ python setup.py install
(env) $ python examples/simple_server.py
```

In another terminal, we can issue calls to the server.

```
(env) $ python examples/simple_client.py
Undefined remote procedure.
3
7
(env) $
```

