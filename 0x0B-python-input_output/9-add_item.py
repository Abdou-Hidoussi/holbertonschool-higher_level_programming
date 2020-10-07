#!/usr/bin/python3
"""holbertontask"""
import sys


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

save_to = "add_item.json"
js = []

if len(sys.argv) > 0:
    try:
        js = load(save_to)
    except FileNotFoundError:
        pass
    save(js + sys.argv[1:], save_to)