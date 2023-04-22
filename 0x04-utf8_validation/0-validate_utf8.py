#!/usr/bin/python3
"""0-validate_utf8 module that implements function validUTF8(data)"""


def count_ones(num):
    """returns the preceding number of binary ones"""
    ones = 0
    for i in range(7, -1, -1):
        if num & (1 << i):
            ones += 1
        else:
            break
    return ones


def validUTF8(data):
    """returns true if data is a valid utf-8 encoding"""
    for i in range(len(data)):
        count = count_ones(data[i])
        if count > 4 or count == 1:
            return False
        if count:
            flag = count - 1
            while flag:
                if data[i + 1] >= 128 and data[i + 1] < 192:
                    i += 1
                    flag -= 1
                    continue
                else:
                    return False
    return True
