import unittest


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_min = self.angleMinute(minutes)
        angle_hour = self.angleHour(hour, minutes)
        angle = abs(angle_hour - angle_min)
        if angle > 180:
            angle = 360 - angle
        return angle

    def angleMinute(self, minutes: int) -> float:
        return 6*minutes

    def angleHour(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        return 30*hour + minutes/2


class TestAngleClock(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_angle_clock_12_30(self):
        hour = 12
        minutes = 30

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 165)

    def test_angle_clock_3_30(self):
        hour = 3
        minutes = 30

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 75)

    def test_angle_clock_3_15(self):
        hour = 3
        minutes = 15

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 7.5)

    def test_angle_clock_4_50(self):
        hour = 4
        minutes = 50

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 155)

    def test_angle_clock_12_00(self):
        hour = 12
        minutes = 0

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 0)

    def test_angle_clock_11_00(self):
        hour = 11
        minutes = 0

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 30)

    def test_angle_clock_10_55(self):
        hour = 10
        minutes = 55

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 2.5)

    def test_angle_clock_3_40(self):
        hour = 3
        minutes = 40

        angle = self.sol.angleClock(hour, minutes)

        self.assertEqual(angle, 130)


if __name__ == "__main__":
    unittest.main()
