import unittest
from typing import List


class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')

        for index in range(len(words)):
            letter = words[index][0]
            if letter == '':
                pass
            elif letter in "aeiouAEIOU":
                words[index] += 'ma' + 'a'*(index+1)
            else:
                if len(words[index]) <= 1:
                    words[index] += 'ma' + 'a'*(index+1)
                else:
                    words[index] = words[index][1:] \
                                  + words[index][0] \
                                  + 'ma' + 'a'*(index+1)

        return ' '.join(words)


class TestToGoatLatin(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testToGoatLatin_1(self):
        S = "I speak Goat Latin"
        exp_goat_latin = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

        act_goat_latin = self.sol.toGoatLatin(S)

        self.assertEqual(act_goat_latin, exp_goat_latin)

    def testToGoatLatin_2(self):
        S = "The quick brown fox jumped over the lazy dog"
        exp_goat_latin = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa"\
                         + " umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa"\
                         + " azylmaaaaaaaaa ogdmaaaaaaaaaa"

        act_goat_latin = self.sol.toGoatLatin(S)

        self.assertEqual(act_goat_latin, exp_goat_latin)


if __name__ == "__main__":
    unittest.main()
