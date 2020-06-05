import unittest
import random
from typing import List


class Solution():
    def __init__(self, w: List[int]):
        self.weights = w
        self.n_weights = len(self.weights)
        self.cum_weights = self.calculate_cumulative_weights(self.weights)
        self.list_index = range(self.n_weights)

    def pickIndex(self) -> int:
        random_number = random.choices(self.list_index,
                                       cum_weights=self.cum_weights)
        return random_number[0]

    def calculate_cumulative_weights(self, weights:  List[int]) -> List[int]:
        sum_weights = 0
        cumulative_weights = []
        for weight in self.weights:
            sum_weights = sum_weights + weight
            cumulative_weights.append(sum_weights)
        return cumulative_weights


# Your Solution object will be instantiated and called as such:
w = [1, 3]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)
