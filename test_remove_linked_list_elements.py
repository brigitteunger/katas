import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while 1:
            if head is None:
                return None
            if head.val == val:
                head = head.next
            else:
                break

        node = head

        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head


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

    def test_remove_element_last_element(self):
        vals = [1, 2, 3, 4, 5, 6]
        val = 6
        head = self.convert_list_2_linked_list(vals)

        rm_head = self.sol.removeElements(head, val)
        rm_vals = self.convert_linked_list_2_list(rm_head)

        self.assertEqual(rm_vals, [1, 2, 3, 4, 5])

    def test_remove_element_first_elelment(self):
        vals = [1, 2, 3, 4, 5, 6]
        val = 1
        head = self.convert_list_2_linked_list(vals)

        rm_head = self.sol.removeElements(head, val)
        rm_vals = self.convert_linked_list_2_list(rm_head)

        self.assertEqual(rm_vals, [2, 3, 4, 5, 6])

    def test_remove_element_no_element(self):
        vals = [1, 2, 3, 4, 5, 6]
        val = 7
        head = self.convert_list_2_linked_list(vals)

        rm_head = self.sol.removeElements(head, val)
        rm_vals = self.convert_linked_list_2_list(rm_head)

        self.assertEqual(rm_vals, [1, 2, 3, 4, 5, 6])

    def test_remove_element_multiple_elements(self):
        vals = [1, 1, 1, 2, 1, 1, 1, 3, 1, 4, 5, 6, 1, 1, 1, 1]
        val = 1
        head = self.convert_list_2_linked_list(vals)

        rm_head = self.sol.removeElements(head, val)
        rm_vals = self.convert_linked_list_2_list(rm_head)

        self.assertEqual(rm_vals, [2, 3, 4, 5, 6])

    def test_remove_element_all_elements(self):
        vals = [1, 1, 1, 1, 1, 1]
        val = 1
        head = self.convert_list_2_linked_list(vals)

        rm_head = self.sol.removeElements(head, val)

        self.assertEqual(rm_head, None)


if __name__ == "__main__":
    unittest.main()
