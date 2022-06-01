import socket

"""Sockets are the end-point of a communication channel

Sockets are low level connectivity.
Connection oriented protocol - TCP
Connectionless protocol - UDP

Higher level connectivity: http, ftp
These run on the application level.

TCP is preffered for sending accurate data
"""

"""create a new socket using socket.socket()
Specify that you want to connect over the internet
by passing socket.AF_INET.
Specify that you want to use TCP protocols
by passing socket.SOCK_STREAM
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""Tell the socket where to connect to
by passing a tuple with the
ip address and port number"""
s.bind(("localhost", 55555))

"""Turn the socket into a server by calling the
.listen() function on the defined socket "s".
This will constantly listen for any clients that
attempt to connect.
"""
s.listen()

"""Create an endless loop that accepts the
connections to the server.
"""
while True:
    client, address = s.accept()
    print(f"Connected to {address}")
    client.send(f"You are connected to {address}".encode())
    # client.close()


def broadcast():
    client.recv
