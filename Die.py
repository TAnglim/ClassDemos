import random
from collections import Counter


class Die:
    "A die"

    def __init__(self, sides=6):
        """Creates a new standard die
        
        Keyword arguments:
        sides (int) -- number of die sides.
        """
        if type(sides) != int or sides < 1:
            raise Exception('sides must be a positive integer.')
        self._sides = sides
        self._rolls = []

    @property
    def rolls(self):
        "history of rolls"
        return self._rolls

    def roll(self):
        "Returns a value between 1 and the number of die sides."
        roll = random.randint(1, self._sides)
        self._rolls.append(roll)
        return roll


def main():
    die = Die()
    rolls = []

    for i in range(100000):
        roll = die.roll()
        rolls.append(roll)

    c = Counter(rolls)
    c_sorted = sorted(c.items())
    print(c_sorted)


if __name__ == "__main__":
    main()
