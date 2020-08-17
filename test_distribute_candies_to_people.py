import unittest
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist_candies = [0]*num_people

        act_cand = 1
        while 1:
            for i in range(num_people):
                if act_cand < candies:
                    dist_candies[i] += act_cand
                    candies -= act_cand
                    act_cand += 1
                else:
                    dist_candies[i] += candies
                    return dist_candies

        return dist_candies


class TestDistibuteCandies(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testDistributeCanides_1(self):
        candies = 7
        num_people = 4

        distributed_candies = self.sol.distributeCandies(candies, num_people)

        self.assertEqual(distributed_candies, [1, 2, 3, 1])

    def testDistributeCanides_2(self):
        candies = 10
        num_people = 3

        distributed_candies = self.sol.distributeCandies(candies, num_people)

        self.assertEqual(distributed_candies, [5, 2, 3])

    def testDistributeCanides_3(self):
        candies = 1
        num_people = 5

        distributed_candies = self.sol.distributeCandies(candies, num_people)

        self.assertEqual(distributed_candies, [1, 0, 0, 0, 0])

    def testDistributeCanides_4(self):
        candies = 1000000000
        num_people = 5

        distributed_candies = self.sol.distributeCandies(candies, num_people)

        self.assertEqual(distributed_candies, [200012864, 199983368, 199992312,
                                               200001256, 200010200])


if __name__ == "__main__":
    unittest.main()
