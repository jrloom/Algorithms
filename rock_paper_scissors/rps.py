#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    # define possible moves
    moves = ["rock", "paper", "scissors"]

    # the list we'll populate, and return
    possible = []

    def rps_recursive(num, list=[]):
        # base case
        if num == 0:
            return possible.append(list)

        else:
            # loop through moves, add to list, repeat until num == 0
            for i in range(len(moves)):
                rps_recursive(num - 1, list + [moves[i]])

        return [possible]

    rps_recursive(n)

    return possible


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
