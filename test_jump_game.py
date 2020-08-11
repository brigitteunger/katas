import unittest
from typing import List
from data_jump_game import nums_1


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        steps_left = 0
        len_nums = len(nums)

        for index in range(len_nums):
            steps_left -= 1
            if steps_left < nums[index]:
                steps_left = nums[index]
            if steps_left + index >= len_nums - 1:
                return True
            if steps_left <= 0:
                return False


class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_can_jump_23114_true(self):
        nums = [2, 3, 1, 1, 4]

        can = self.sol.canJump(nums)

        self.assertTrue(can)

    def test_can_jump_32104_false(self):
        nums = [3, 2, 1, 0, 4]

        can = self.sol.canJump(nums)

        self.assertFalse(can)

    def test_can_jump_0_true(self):
        nums = [0]

        can = self.sol.canJump(nums)

        self.assertTrue(can)

    def test_can_jump_123_true(self):
        nums = [1, 2, 3]

        can = self.sol.canJump(nums)

        self.assertTrue(can)

    def test_can_jump_1201_true(self):
        nums = [1, 2, 0, 1]

        can = self.sol.canJump(nums)

        self.assertTrue(can)

    def test_can_jump_first_long_true(self):
        nums = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]

        can = self.sol.canJump(nums)

        self.assertTrue(can)

    def test_can_jump_long(self):
        nums = nums_1

        can = self.sol.canJump(nums)

        self.assertFalse(can)


if __name__ == "__main__":
    unittest.main()
