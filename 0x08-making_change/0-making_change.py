#!/usr/bin/python3
"""making_change module
"""


def makeChange(coins, total):
    """returns fewest possible number of coins
       Args:
           coins: list of coins at hand
           total: total amount to make change
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num = 0
    for coin in coins:
        if coin <= total:
            num += total // coin
            total = total % coin
    if total != 0:
        return -1
    return num
