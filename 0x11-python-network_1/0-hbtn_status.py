#!/usr/bin/python3
""" Task 0 """
import urllib.request


print("Body response:")
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
