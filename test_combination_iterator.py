import unittest
from typing import List


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int) -> None:
        self.index = 0
        self.comb_list = self.generate_combinations(characters,
                                                    combinationLength)
        self.len_list = len(self.comb_list)

    def generate_combinations(self,
                              characters: str,
                              combinationLength: int
                              ) -> List[str]:
        if not characters:
            return []
        char_list = list(characters)
        char_list.sort()
        len_char = len(char_list)
        masks = self.generate_masks(len_char, combinationLength)
        comb_list = []
        for mask in masks:
            combination = ''
            for index in range(len_char):
                if mask[index] == '1':
                    combination += char_list[index]
            comb_list.append(combination)

        return comb_list

    def generate_masks(self,
                       bits_mask: int,
                       combinationLength: int
                       ) -> List[List[int]]:
        masks = []
        max_num = (2**bits_mask) - 1

        for num in range(max_num, -1, -1):
            format_mask = '{:0'+str(bits_mask)+'b}'
            mask = list(format_mask.format(num))
            if mask.count('1') == combinationLength:
                masks.append(mask)

        return masks

    def next_(self) -> str:
        if self.index == self.len_list:
            return None
        else:
            elem = self.comb_list[self.index]
            self.index += 1
        return elem

    def hasNext(self) -> bool:
        if self.index == self.len_list:
            return False
        else:
            return True


class TestCombinationIterator(unittest.TestCase):
    def test_generate_masks(self):
        obj = CombinationIterator("abc", 2)
        masks = obj.generate_masks(3, 2)
        self.assertEqual(masks,
                         [['1', '1', '0'],
                          ['1', '0', '1'],
                          ['0', '1', '1']]
                         )

    def test_generate_combinations(self):
        obj = CombinationIterator("abc", 2)
        combinations = obj.generate_combinations("abc", 2)
        self.assertEqual(combinations, ['ab', 'ac', 'bc'])

    def testCombinationIterator_1(self):
        obj = CombinationIterator("abc", 2)
        self.assertEqual(obj.next_(), "ab")
        self.assertTrue(obj.hasNext())
        self.assertEqual(obj.next_(), "ac")
        self.assertTrue(obj.hasNext())
        self.assertEqual(obj.next_(), "bc")
        self.assertFalse(obj.hasNext())


if __name__ == "__main__":
    unittest.main()
