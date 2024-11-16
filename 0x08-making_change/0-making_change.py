#!/usr/bin/python3
"""A greedy way to solve the coin change problem...

    Why not submitting the DP version {Which is fun an easy}.. Who knows?
"""


def makeChange(coins, amount):
    """
    Greedy solution for teh coin change
    """
    if amount <= 0:
        return 0

    total_coins = 0
    coins.sort(reverse=True)
    for coin in coins:
        if amount == 0:
            break

        num_coins = amount // coin
        amount -= num_coins * coin
        total_coins += num_coins

    return -1 if amount != 0 else total_coins
