import random

# The Coin class simulates a coin that can
# be flipped.

# class is a reserved word in python
# use upper case for your object definition
# init (short for initialization) is always first


class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.__sideup = "Heads"  # attribute

    # to hide an attribute, add two underscores before the attribute name
    # mutator method--we want the method to control the attribute
    # aka set method (as opposed to get methods)
    # mutator changes value of attribute, accessor just looks at it

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):  # method
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"  # attribute
        else:
            self.__sideup = "Tails"

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):  # method
        return self.__sideup  # attribute
