import random


class Insect:
    # initialize attributes
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight_len = 0

    # create method
    def create_flight_len(self):
        self.flight_len = random.randint(1, 10)

    # another one
    def get_flight_len(self):
        return self.flight_len
