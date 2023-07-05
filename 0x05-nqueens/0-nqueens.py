#!/usr/bin/python3
"""n-queens module
"""
from sys import argv


# def is_valid()

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except Exception:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
