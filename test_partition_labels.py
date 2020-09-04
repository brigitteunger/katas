import unittest
from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return [0]
        len_S = len(S)
        len_partitions = []
        sum_partitions = 0
        S_list = list(S)
        while 1:
            len_new_partition = self.findPartition(S_list[sum_partitions:])
            len_partitions.append(len_new_partition)
            sum_partitions += len_new_partition
            if sum_partitions >= len_S:
                break
        return len_partitions

    def findPartition(self, letters: List[str]) -> int:
        len_letters = len(letters)
        if len_letters == 1:
            return 1

        highest_index = self.findHighestIndex(letters, letters[0])

        while 1:
            dict_partition = Counter(letters[0:highest_index+1])
            refresh_dict = False
            for key in dict_partition.keys():
                key_index = self.findHighestIndex(letters, key)
                if highest_index < key_index:
                    highest_index = key_index
                    refresh_dict = True
                    break
            if not refresh_dict:
                break
        return highest_index+1

    def findHighestIndex(self, letters: List[str], letter) -> int:
        reversed_letters = list(reversed(letters))
        return len(letters) - reversed_letters.index(letter) - 1


class TestPartitionLabels(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testPartitionLabels_1(self):
        S = "ababcbacadefegdehijhklij"

        partitions = self.sol.partitionLabels(S)

        self.assertEqual(partitions, [9, 7, 8])

    def testPartitionLabels_2(self):
        S = "ababcbacadaefegdehijhklij"

        partitions = self.sol.partitionLabels(S)

        self.assertEqual(partitions, [17, 8])

    def testPartitionLabels_3(self):
        S = "ababcbacadaefegdehijhklij"

        partitions = self.sol.partitionLabels(S)

        self.assertEqual(partitions, [17, 8])

    def testPartitionLabels_4(self):
        S = "ab"

        partitions = self.sol.partitionLabels(S)

        self.assertEqual(partitions, [1, 1])

    def testPartitionLabels_5(self):
        S = "a"

        partitions = self.sol.partitionLabels(S)

        self.assertEqual(partitions, [1])


if __name__ == "__main__":
    unittest.main()
