import unittest
from data_target_component_size_by_common_factor import A2
from collections import defaultdict
from typing import Dict, List


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        count_for_factor = defaultdict(lambda: 0)
        components = {}

        for num in A:
            if num == 1:
                count_for_factor[1] += 1
            else:
                factors = self.prime_factors(num)
                len_factors = len(factors)
                if len_factors > 1:
                    for i in range(len_factors - 1):
                        for j in range(i + 1, len_factors):
                            self.union(factors[i], factors[j], components)
                count_for_factor[factors[0]] += 1

        sizes = defaultdict(lambda: 0)
        for factor, count in count_for_factor.items():
            self.update_parents(factor, components)
            component = components[factor]
            sizes[component] += count
        return max(sizes.values())

    def union(self, firstFactor: int, secondFactor: int,
              components: Dict[int, int]) -> None:
        self.update_parents(firstFactor, components)
        self.update_parents(secondFactor, components)
        if components[firstFactor] > components[secondFactor]:
            components[components[firstFactor]] = components[secondFactor]
        else:
            components[components[secondFactor]] = components[firstFactor]

    def update_parents(self, factor: int, components: Dict[int, int]) -> None:
        if factor in components:
            component = components[factor]
            if component != factor:
                components[factor] = components[component]
        else:
            components[factor] = factor

    def prime_factors(self, n: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                while n % i == 0:
                    n /= i
                if i not in factors:
                    factors.append(i)
        if n > 1:
            if n not in factors:
                factors.append(n)
        return factors


class TestLargestComponentSize(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLargestComponentSize_1(self):
        A = [4, 6, 15, 35]

        largest = self.sol.largestComponentSize(A)

        self.assertEqual(largest, 4)

    def testLargestComponentSize_2(self):
        A = [20, 50, 9, 63]

        largest = self.sol.largestComponentSize(A)

        self.assertEqual(largest, 2)

    def testLargestComponentSize_3(self):
        A = [2, 3, 6, 7, 4, 12, 21, 39]

        largest = self.sol.largestComponentSize(A)

        self.assertEqual(largest, 8)

    def testLargestComponentSize_4(self):
        A = A2

        largest = self.sol.largestComponentSize(A)

        self.assertEqual(largest, 16998)

    def testLargestComponentSize_5(self):
        A = [83, 99, 39, 11, 19, 30, 31]

        largest = self.sol.largestComponentSize(A)

        self.assertEqual(largest, 4)


if __name__ == "__main__":
    unittest.main()
