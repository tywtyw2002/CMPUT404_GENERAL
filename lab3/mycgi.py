#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
# work with python 2.7

import sys ,os, cgi

print "Hello"

print "Content-type: text/html"
print ""
print "<HTML><BODY><FORM method='POST'><INPUT name='x'></FORM></BODY></HTML>"
print ""

form = cgi.FieldStorage()
print form.getvalue('x')
