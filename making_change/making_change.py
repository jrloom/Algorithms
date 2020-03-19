#!/usr/bin/python

import sys


def making_change(amount, denominations):

    # initialize cache
    possible = [0] * (amount + 1)
    # print(f"initial cache: {possible}")

    # 0 cents
    possible[0] = 1

    # first loop returns possibilities
    for val in denominations:
        # loop through higher amounts between val and amount
        for higher_amount in range(1, amount + 1):
            if val <= higher_amount:
                # if denom <= current, add to possible
                possible[higher_amount] += possible[higher_amount - val]
                # print(f"val {val} | ha {higher_amount}")
                # print(f"cache: {possible}")
                # print("\n--------------------\n")

    return possible[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")
