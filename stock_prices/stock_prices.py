#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # we're going to track the current min price
    current_min_price_so_far = prices[0]

    # we're also going to track the current max profit
    max_profit_so_far = prices[1] - prices[0]

    # comparison loop
    for i in range(1, len(prices)):

        # if (current index) < (current min price),
        if prices[i] < current_min_price_so_far:
            # update (current min price) to equal (current index)
            current_min_price_so_far = prices[i]

        # if (current index) - (current min price) > (current max profit),
        elif prices[i] - current_min_price_so_far > max_profit_so_far:
            # update (current max profit) to equal (current index) - (current min price)
            max_profit_so_far = prices[i] - current_min_price_so_far

    return max_profit_so_far


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )
