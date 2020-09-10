import unittest
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        len_guess = len(guess)
        bulls = 0

        for index in range(len_guess-1, -1, -1):
            if secret[index] == guess[index]:
                bulls += 1

        cows = -bulls
        guess_dict = Counter(guess)
        secret_dict = Counter(secret)

        for key in guess_dict.keys():
            if key in secret_dict:
                cows += min(guess_dict[key], secret_dict[key])

        return str(bulls) + "A" + str(cows) + "B"


class TestGetHint(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testGetHint1(self):
        secret = "1807"
        guess = "7810"

        hint = self.sol.getHint(secret, guess)

        self.assertEqual(hint, "1A3B")

    def testGetHint2(self):
        secret = "1123"
        guess = "0111"

        hint = self.sol.getHint(secret, guess)

        self.assertEqual(hint, "1A1B")

    def testGetHint3(self):
        secret = "1807"
        guess = "3333"

        hint = self.sol.getHint(secret, guess)

        self.assertEqual(hint, "0A0B")


if __name__ == "__main__":
    unittest.main()
