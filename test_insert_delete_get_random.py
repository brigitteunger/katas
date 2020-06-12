import unittest
import random
from typing import List


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ran_set = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val in self.ran_set:
            return False
        else:
            self.ran_set.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val in self.ran_set:
            self.ran_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.ran_set:
            return None
        else:
            return random.choice(self.ran_set)


class TestRandomizedSet(unittest.TestCase):
    def test_getRandom_insert_true(self):
        randomSet = RandomizedSet()

        feedback = randomSet.insert(1)

        self.assertTrue(feedback)

    def test_getRandom_remove_false(self):
        randomSet = RandomizedSet()

        feedback = randomSet.remove(2)

        self.assertFalse(feedback)

    def test_getRandom_remove_true(self):
        randomSet = RandomizedSet()
        randomSet.insert(1)

        feedback = randomSet.remove(1)

        self.assertTrue(feedback)

    def test_getRandom_insert_same_twice(self):
        randomSet = RandomizedSet()
        randomSet.insert(2)

        feedback = randomSet.insert(2)

        self.assertFalse(feedback)


if __name__ == "__main__":
    unittest.main()
