#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
# work with python 2.7

import requests

print requests.__version__

response = requests.get("http://www.google.ca")

print response.status_code
#print response.text
