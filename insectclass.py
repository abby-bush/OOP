import random


class Insect:
    # initialize attributes
    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    # create method
    def flight_len(self):
        self.flight = random.randint(1, 10)

    # another one
    def get_miles(self):
        return self.flight

    def get_name(self):
        return self.name
