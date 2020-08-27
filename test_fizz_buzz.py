import unittest
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strings = []
        for num in range(1, n+1):
            mod_3 = (num % 3 == 0)
            mod_5 = (num % 5 == 0)
            if mod_3:
                if mod_5:
                    strings.append('FizzBuzz')
                    continue
                else:
                    strings.append('Fizz')
            elif mod_5:
                strings.append('Buzz')
            else:
                strings.append(str(num))

        return strings


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFizzBuzz_1(self):
        n = 15

        strings = self.sol.fizzBuzz(n)

        self.assertEqual(strings,
                         ["1",
                          "2",
                          "Fizz",
                          "4",
                          "Buzz",
                          "Fizz",
                          "7",
                          "8",
                          "Fizz",
                          "Buzz",
                          "11",
                          "Fizz",
                          "13",
                          "14",
                          "FizzBuzz"]
                         )

    def testFizzBuzz_2(self):
        n = 0

        strings = self.sol.fizzBuzz(n)

        self.assertEqual(strings, [])


if __name__ == "__main__":
    unittest.main()
