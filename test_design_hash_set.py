import unittest
from typing import List


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_num_hashes = 2**10
        self.my_table = [[]] * self.max_num_hashes

    def add(self, key: int) -> None:
        index = self.my_hash_function(key)
        if key not in self.my_table[index]:
            self.my_table[index].append(key)

    def remove(self, key: int) -> None:
        index = self.my_hash_function(key)
        for i in range(len(self.my_table[index])):
            if self.my_table[index][i] == key:
                del self.my_table[index][i]
                break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.my_hash_function(key)
        for i in range(len(self.my_table[index])):
            if self.my_table[index][i] == key:
                return True
        return False

    def my_hash_function(self, key: int) -> int:
        my_hash = key % self.max_num_hashes
        return my_hash


class TestMyHashSet(unittest.TestCase):
    def setUp(self):
        self.obj = MyHashSet()

    def test_add_contains_True(self):
        self.obj.add(1)
        self.assertTrue(self.obj.contains(1))

    def test_add_contains_False(self):
        self.obj.add(1)
        self.obj.add(2)
        self.assertFalse(self.obj.contains(3))

    def test_add_contains_remove_True(self):
        self.obj.add(1)
        self.assertTrue(self.obj.contains(1))
        self.obj.remove(1)
        self.assertFalse(self.obj.contains(1))

    def test_add_contains_remove_False(self):
        self.obj.add(1)
        self.assertTrue(self.obj.contains(1))
        self.obj.remove(10)
        self.assertTrue(self.obj.contains(1))

    def test_add_contains_remove_Final(self):
        self.obj.add(1)
        self.obj.add(2)
        self.assertTrue(self.obj.contains(1))
        self.assertFalse(self.obj.contains(3))
        self.obj.add(2)
        self.assertTrue(self.obj.contains(2))
        self.obj.remove(2)
        self.assertFalse(self.obj.contains(2))


if __name__ == "__main__":
    unittest.main()
