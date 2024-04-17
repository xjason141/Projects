#!/usr/bin/env python3

import requests

#Shows how a file can be uploaded using the Python requests module

url = 'http://localhost/upload/'
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})