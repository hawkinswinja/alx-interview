#!/usr/bin/python3
"""making_change module
"""


def makeChange(coins, total):
    """returns fewest possible number of coins
       Args:
           coins: list of coins at hand
           total: total amount to make change
    """
    if not total or len(coins) <= 0:
        return 0
    coins.sort()
    num = [float('inf')] * (total + 1)
    num[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            num[i] = min(num[i], num[i - coin] + 1)
    if num[total] == float('inf'):
        return -1
    return num[total]
