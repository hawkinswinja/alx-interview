#!/usr/bin/python3
"""log-parser"""
import re
import sys


def display(fs, mydict):
    print(f'File size: {fs}')
    for k, v in mydict.items():
        if v > 0:
            print(f'{k}: {v}')

n = 0
filesize = 0
mydict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        n += 1
        if not re.search(r'^(\d{1,3}\.){3}\d{1,3} - ', line):
            continue
        log = line.split(' ')[-2:]
        filesize += int(log[-1])
        try:
            mydict[int(log[0])] += 1
        except Exception:
            pass
        if n == 10:
            display(filesize, mydict)
            n = 0
except Exception:
    pass
finally:
    display(filesize, mydict)
    