#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = []
print(data)
print(validUTF8(data), '\n\n')
data = [65]
print(data)
print(validUTF8(data), '\n\n')
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(data)
print(validUTF8(data), '\n\n')
data = [229, 65, 127, 256]
print(data)
print(validUTF8(data), '\n\n')
