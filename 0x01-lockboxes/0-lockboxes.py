#!/usr/bin/python3
"""This module contains a single function canUnlockAll(boxes)"""


def canUnlockAll(boxes):
    """Checks if all boxes in mylist can be unlocked"""
    opened = [0]
    n =len(boxes)
    for key in range(1, n):
        if key in boxes[0]:
            opened.append(key)
            boxes[0] += boxes[key]
    if len(opened) == n:
        return True
    for i in range(1,n):
        if i in opened:
            continue
        if i in set(boxes[0]):
            opened.append(i)
            boxes[0] += boxes[i]
        else:
            return False
    return True
