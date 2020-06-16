import unittest
import string
# from typing import List


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP is None:
            return "Neither"

        if "." in IP:
            return self.validIP4Adress(IP)
        elif ":" in IP:
            return self.validIP6Adress(IP)
        return "Neither"

    def validIP4Adress(self, IP: str) -> str:
        nums_list = IP.split('.')

        if len(nums_list) != 4:
            return "Neither"

        for num in nums_list:
            # Test number?
            is_number = all(letter in string.digits for letter in num)
            if not is_number:
                return "Neither"
            num_list = list(num)
            size_num_list = len(num_list)
            if size_num_list > 3 or size_num_list < 1:
                return "Neither"
            elif size_num_list == 3:
                if num_list[0] == '0':
                    return "Neither"
            elif size_num_list == 2:
                if num_list[0] == '0':
                    return "Neither"

            if int(num) > 255:
                return "Neither"

        return "IPv4"

    def validIP6Adress(self, IP: str) -> str:
        nums_list = IP.split(':')

        if len(nums_list) != 8:
            return "Neither"

        for num in nums_list:
            size_num_list = len(num)
            if size_num_list < 1 or size_num_list > 4:
                return "Neither"
            # Test hex number?
            hex_dig = all(letter in string.hexdigits for letter in num)
            if not hex_dig:
                return "Neither"

        return "IPv6"


class TestValidIPAdress(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid_ip_address_IP4_valid(self):
        IP = "172.16.254.1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "IPv4")

    def test_valid_ip_address_IP4_invalid_basis_e(self):
        IP = "1e1.4.5.6"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_valid_no_number(self):
        IP = "0.0.0.-1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_valid_with_zero(self):
        IP = "172.0.254.1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "IPv4")

    def test_valid_ip_address_IP4_invalid_lead_zero(self):
        IP = "172.16.254.01"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_invalid_lead_zero_three_nums(self):
        IP = "172.016.254.1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_invalid_lead_zero_four_nums(self):
        IP = "172.0116.254.1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_invalid_to_high(self):
        IP = "172.16.256.1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_invalid_empty_number(self):
        IP = "172.16..1"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP4_invalid_not_enough(self):
        IP = "172.16.01"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_invalid_empty_string(self):
        IP = ""

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_invalid_no_separators(self):
        IP = "172162561"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "Neither")

    def test_valid_ip_address_IP6_valid_with_lead_zeros(self):
        IP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip, "IPv6")

    def test_valid_ip_address_IP6_valid_without_leading_zeros(self):
        IP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip,  "IPv6")

    def test_valid_ip_address_IP6_invalid_with_leading_zeros(self):
        IP = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip,  "Neither")

    def test_valid_ip_address_IP6_invalid_no_number(self):
        IP = "2001:0db8:85a3::8A2E:0370:7334:0a23"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip,  "Neither")

    def test_valid_ip_address_IP6_invalid_number(self):
        IP = "2001:0db8:85a3:451:8G2E:0370:7334:125"

        str_ip = self.sol.validIPAddress(IP)

        self.assertEqual(str_ip,  "Neither")


if __name__ == "__main__":
    unittest.main()
