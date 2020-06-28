import unittest
from typing import List, Dict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        itinerary = []
        adjacency_tickets = self.build_adjacency_tickets(tickets)
        departure = 'JFK'
        trail = [departure]

        while 1:
            if departure not in adjacency_tickets:
                itinerary.insert(0, departure)
                del trail[-1]
                if not trail:
                    break
                departure = trail[-1]
            else:
                arrival = adjacency_tickets[departure].pop(0)
                if not adjacency_tickets[departure]:
                    del adjacency_tickets[departure]
                trail.append(arrival)
                departure = arrival

        return itinerary

    def build_adjacency_tickets(self,
                                tickets: List[List[str]]
                                ) -> Dict[str, str]:
        dict_tickets = {}
        for ticket in tickets:
            departure = ticket[0]
            arrival = ticket[1]
            if departure in dict_tickets:
                dict_tickets[departure].append(arrival)
                dict_tickets[departure].sort()
            else:
                dict_tickets[departure] = [arrival]
        return dict_tickets


class TestFindtinerary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_find_itinerary_0(self):
        tickets = []

        itinerary = self.sol.findItinerary(tickets)

        self.assertEqual(
            itinerary,
            []
        )

    def test_find_itinerary_0_1(self):
        tickets = [["JFK", "MUC"]]

        itinerary = self.sol.findItinerary(tickets)

        self.assertEqual(
            itinerary,
            ["JFK", "MUC"]
        )

    def test_find_itinerary_1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"],
                   ["LHR", "SFO"]]

        itinerary = self.sol.findItinerary(tickets)

        self.assertEqual(
            itinerary,
            ["JFK", "MUC", "LHR", "SFO", "SJC"]
        )

    def test_find_itinerary_2(self):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                   ["ATL", "JFK"], ["ATL", "SFO"]]

        itinerary = self.sol.findItinerary(tickets)

        self.assertEqual(
            itinerary,
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        )


if __name__ == "__main__":
    unittest.main()
