#!/usr/bin/python

# 0:  0 cookie * 1 time
# 1:  1 cookie * 1 time
# 2:  1 cookie * 2 times  ||  2 cookies * 1 time
# 3:  1 cookie * 3 times  ||  2 cookies * 1 time + 1 cookie * 1 time  ||  1 cookie * 1 time + 2 cookies * 1 time  ||  3 cookies * 1 time


import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# def eating_cookies(n, cache={}):

# base cases

# if n < 0:
#     return 0

# elif n == 0:
#     return 1

# elif n not in cache:
#     cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

# return cache[n]


def eating_cookies(n, cache=None):

    if n < 0:
        return 0

    elif n == 0:
        return 1

    elif cache and cache[n] > 0:
        return cache[n]

    else:
        if cache is None:
            cache = {}

        value = (
            eating_cookies(n - 1, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 3, cache)
        )

        cache[n] = value

        return value


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")
