#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
# work with python 2.7

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("www.google.ca",80))

request = "GET / HTTP/1.0\n\n"

client_socket.sendall(request)

done = True

while done:
    part = client_socket.recv(2048)
    if part:
        print part
    else:
        done = False
