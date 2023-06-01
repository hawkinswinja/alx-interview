#!/usr/bin/python3
"""module 0-prime_game"""


def isWinner(x, nums):
    """returns the game winner of the prime_game
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def multiples(mylist, x):
    """remove multiples of prime x"""
    for i in range(2, len(mylist)):
        try:
            mylist[i * x] = 0
        except (ValueError, IndexError):
            break
