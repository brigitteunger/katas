import unittest
from typing import List, Dict
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_elem = Counter(nums)
        size_majority = len(nums)//3
        list_majortity = []
        for key, item in dict_elem.items():
            if item > size_majority:
                list_majortity.append(key)
        return list_majortity


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMajorityElement_1(self):
        nums = [3, 2, 3]

        actual = self.sol.majorityElement(nums)

        self.assertEqual(actual, [3])

    def testMajorityElement_2(self):
        nums = [1, 1, 1, 3, 3, 2, 2, 2]

        actual = self.sol.majorityElement(nums)

        self.assertEqual(actual, [1, 2])


if __name__ == "__main__":
    unittest.main()
