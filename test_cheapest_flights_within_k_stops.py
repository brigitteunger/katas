import unittest
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        if not flights:
            return -1

        max_val = 10000*n + 1

        prices_to_city = {}
        prices_to_city[src] = {0: 0}
        connections_per_city = []
        for _ in range(n):
            connections_per_city.append([])

        # group flights by start city
        for flight in flights:
            connections_per_city[flight[0]].append(flight)

        # add prices without layover in table prices_to_city
        for flight in connections_per_city[src]:
            key = flight[1]
            prices_to_city[key] = {0: flight[2]}

        # add prices according to layover ...
        for layover in range(1, K+1):
            for start_city in range(0, n):
                if src == start_city:
                    continue
                for connection in connections_per_city[start_city]:
                    dest_city = connection[1]
                    price_start_dest = connection[2]
                    if (start_city in prices_to_city.keys() and
                            layover-1 in prices_to_city[start_city].keys()):
                        price_0_dest = (prices_to_city[start_city][layover-1]
                                        + price_start_dest)

                        min_price = max_val
                        if dest_city in prices_to_city.keys():
                            if layover in prices_to_city[dest_city].keys():
                                min_price = prices_to_city[dest_city][layover]

                        if min_price > price_0_dest:
                            if dest_city in prices_to_city:
                                prices_to_city[dest_city][layover] = (
                                    price_0_dest)
                            else:
                                prices_to_city[dest_city] = {layover:
                                                             price_0_dest}
        if dst in prices_to_city:
            return min(prices_to_city[dst].values())
        else:
            return -1


class TestFindCheapestPrice(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_cheapest_price_six_knotes_k2(self):
        n = 6
        flights = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1],
                   [4, 5, 1], [1, 3, 10], [3, 5, 10]]
        src = 0
        dst = 5
        k = 2

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, 21)

    def test_find_cheapest_price_k1(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, 200)

    def test_find_cheapest_price_k0(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, 500)

    def test_find_cheapest_price_no_solution(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100]]
        src = 0
        dst = 2
        k = 0

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, -1)

    def test_find_cheapest_price_many_knotes_k1(self):
        n = 5
        flights = [[0, 1, 10], [1, 4, 500], [0, 2, 10], [2, 3, 30],
                   [3, 4, 50], [2, 1, 20], [2, 4, 200]]
        src = 0
        dst = 4
        k = 1

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, 210)

    def test_find_cheapest_price_many_knotes_k3(self):
        n = 5
        flights = [[0, 1, 10], [1, 4, 500], [0, 2, 10], [2, 3, 30],
                   [3, 4, 50], [2, 1, 20], [2, 4, 200]]
        src = 0
        dst = 4
        k = 3

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, 90)

    def test_find_cheapest_price_many_six_sth(self):
        n = 5
        flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1],[1, 4, 3]]
        src = 2
        dst = 1
        k = 1

        price = self.sol.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(price, -1)


if __name__ == "__main__":
    unittest.main()
