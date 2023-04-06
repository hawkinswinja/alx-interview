#!/usr/bin/python3
"""This module contains a single function minOperations"""


def minOperations(n):
    """Calculate the lowest no. of steps to get H"""
    cp = 2
    steps = 0
    #check for edge cases
    while n > 1:
        while n % cp == 0:
            steps += cp
            n /= cp
        cp += 1
    return steps
