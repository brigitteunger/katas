import unittest
from data_serialize_deserialize_BST import data_1
from typing import List, Deque
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        vals = []
        self.__build_list__(vals, root)
        return ','.join(vals)

    def __build_list__(self, vals, root):
        if root is None:
            vals.append('_')
        else:
            vals.append(str(root.val))
            self.__build_list__(vals, root.left)
            self.__build_list__(vals, root.right)

    def deserialize(self, data):
        vals = list(data.split(','))
        vals.reverse()
        return self.__build_tree__(None, vals)

    def __build_tree__(self, root, vals):
        if vals:
            key = vals.pop()
            if key != '_':
                root = TreeNode(int(key))
                root.left = self.__build_tree__(root.left, vals)
                root.right = self.__build_tree__(root.right, vals)
        return root


class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def testCodec_1(self):
        data = "1,2,3,4,5,6,_,_,_,_,_,_,_"

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)

    def testCodec_2(self):
        data = "_"

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)

    def testCodec_3(self):
        data = "1,_,_"

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)

    def testCodec_4(self):
        data = "1,2,_,_,_"

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)

    def testCodec_5(self):
        data = "1,_,2,_,_"

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)

    def testCodec_6(self):
        data = data_1

        root = self.codec.deserialize(data)
        data_processed = self.codec.serialize(root)

        self.assertEqual(data, data_processed)


if __name__ == "__main__":
    unittest.main()
