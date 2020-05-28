import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        all_list = []
        for linked_list in lists:
            all_list = all_list + self.convert_list_2_linked_list(linked_list)
        all_list.sort()
        head = self.convert_linked_list_2_list(all_list)
        return head

    def convert_list_2_linked_list(self, vals: list) -> ListNode:
        node = None
        for val in reversed(vals):
            node = ListNode(val, node)
        return node

    def convert_linked_list_2_list(self, node: ListNode) -> list:
        vals = []
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals


class TestListNode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def convert_list_2_linked_list(self, vals: list) -> ListNode:
        node = None
        for val in reversed(vals):
            node = ListNode(val, node)
        return node

    def convert_linked_list_2_list(self, node: ListNode) -> list:
        vals = []
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals

    def test_convertion(self):
        vals = [4, 3, 5]

        linked_vals = self.convert_list_2_linked_list(vals)
        vals_processed = self.convert_linked_list_2_list(linked_vals)

        self.assertEqual(vals_processed, vals_processed)

    def create_list_linked_lists(self, list_lists: list) -> List[ListNode]:
        list_linked_lists = []
        for list_n in list_lists:
            linked_list = self.convert_list_2_linked_list(list_n)
            list_linked_lists.append(linked_list)
        return list_linked_lists

    def test_merge_k_lists(self):
        list_lists = []
        list_lists.append([1, 4, 5])
        list_lists.append([1, 3, 4])
        list_lists.append([2, 6])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [1, 1, 2, 3, 4, 4, 5, 6]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_all_equal(self):
        list_lists = []
        list_lists.append([1, 1, 1])
        list_lists.append([1, 1, 1])
        list_lists.append([1, 1, 1])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [1, 1, 1, 1, 1, 1, 1, 1, 1]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_two_lists(self):
        list_lists = []
        list_lists.append([-5, 1, 4])
        list_lists.append([1, 3, 4])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [-5, 1, 1, 3, 4, 4]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_four_lists(self):
        list_lists = []
        list_lists.append([-30, 0, 0])
        list_lists.append([-5, 1, 4])
        list_lists.append([1, 3, 4])
        list_lists.append([-6, -5, -3, 2, 2, 6, 100])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [-30, -6, -5, -5, -3, 0, 0, 1, 1, 2, 2, 3, 4, 4, 6,
                         100]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_one_list(self):
        list_lists = []
        list_lists.append([1, 4, 5])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [1, 4, 5]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_empty_list(self):
        list_lists = []
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = []

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_one_empty_list(self):
        list_lists = []
        list_lists.append([])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = []

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_one_list_one_element(self):
        list_lists = []
        list_lists.append([1])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = [1]

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)

    def test_merge_k_lists_two_empty_lists(self):
        list_lists = []
        list_lists.append([])
        list_lists.append([])
        list_linked_lists = self.create_list_linked_lists(list_lists)
        merged_result = []

        merged_linked_list = self.sol.merge_k_lists(list_linked_lists)
        merged_list = self.convert_linked_list_2_list(merged_linked_list)

        self.assertEqual(merged_list, merged_result)


test_ = TestListNode()
test_.test_convertion()
