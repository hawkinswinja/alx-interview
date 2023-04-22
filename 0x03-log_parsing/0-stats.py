#!/usr/bin/python3
"""log-parser: summary of number of requests sent"""
import re
import sys


def display(fs, mydict):
    """prints the summary to stdout"""
    print('File size: {}'.format(fs))
    for k, v in mydict.items():
        if v > 0:
            print('{}: {}'.format(k, v))

n = 0
filesize = 0
mydict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
date =  '\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]'
protocol = ' "GET /projects/260 HTTP/1.1"'
target = '.+ - ' + date + protocol + ' (?P<code>\d{3})' + ' (?P<size>\d+)'
try:
    for line in sys.stdin:
        n += 1
        data = re.match(target, line)
        if data:
            data = data.groupdict()
            filesize += int(data.get('size'))
        try:
            mydict[int(data.get('code'))] += 1
        except Exception:
            pass
        if n == 10:
            display(filesize, mydict)
            n = 0
except KeyboardInterrupt:
    display(filesize, mydict)
