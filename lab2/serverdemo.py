#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
# work with python 2.7

import socket, os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)

while True:
    client, addr = server_socket.accept()

    child_pid = os.fork()
    if (child_pid != 0):
        continue

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    remote_socket. connect(("www.google.ca",80))

    done = True
    while done:

        client.setblocking(0)
        try:
            part = client.recv(2048)
        except IOError, exception:
            if exception.errno == 11:
                part = None
            else:
                raise
        if part:
            remote_socket.sendall(part)


        remote_socket.setblocking(0)
        try:
            part = remote_socket.recv(2048)
        except IOError, exception:
            if exception.errno == 11:
                part = None
            else:
                raise
        if part:
            client.sendall(part)
