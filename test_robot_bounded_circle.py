import unittest


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = "N"
        vector = [0, 0]
        for instruction in instructions:
            if instruction == "G":
                if direction == "N":
                    vector[1] += 1
                elif direction == "E":
                    vector[0] += 1
                elif direction == "S":
                    vector[1] -= 1
                else:  # W
                    vector[0] -= 1
            elif instruction == "R":
                if direction == "N":
                    direction = "E"
                elif direction == "E":
                    direction = "S"
                elif direction == "S":
                    direction = "W"
                else:  # W
                    direction = "N"
            else:  # "L"
                if direction == "N":
                    direction = "W"
                elif direction == "E":
                    direction = "N"
                elif direction == "S":
                    direction = "E"
                else:  # W
                    direction = "S"

        if direction != "N":
            return True
        elif vector[0] == 0 and vector[1] == 0:
            return True
        else:
            return False


class TestRobotBoundedCircle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testIsRobotBounded_1(self):
        instructions = "GGLLGG"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertTrue(is_circle)

    def testIsRobotBounded_2(self):
        instructions = "GG"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertFalse(is_circle)

    def testIsRobotBounded_3(self):
        instructions = "GL"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertTrue(is_circle)

    def testIsRobotBounded_4(self):
        instructions = "L"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertTrue(is_circle)

    def testIsRobotBounded_5(self):
        instructions = "GLGLGGLGL"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertFalse(is_circle)

    def testIsRobotBounded_6(self):
        instructions = "GLRLLGLL"

        is_circle = self.sol.isRobotBounded(instructions)

        self.assertTrue(is_circle)


if __name__ == "__main__":
    unittest.main()
