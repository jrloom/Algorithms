#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # track batches - start with an empty list that we'll add stuff to bsaed on the criteria below
    batches = []

    for i in recipe:

        # check ingredients
        if i not in ingredients:
            # print("nope")
            return 0

        # if (on-hand ingredients) / (amount needed) is >= 1
        elif ingredients[i] // recipe[i] >= 1:
            # add that to the batches list
            batches.append(ingredients[i] // recipe[i])
            # print(f"bacthes: {batches}")

    return min(batches)


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )
