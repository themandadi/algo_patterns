#!/usr/bin/env python3

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # def in_order(root):
        #     output = []
        #     stack = []

        #     while root or stack:
        #         while root:
        #             stack.append(root)
        #             root = root.left
                
        #         root = stack.pop()
        #         output.append(root.val)
        #         root = root.right
        #     return output
        
        # out = in_order(root)
        # return out[k-1]

        result = []

        def in_order(node):

            if not node:
                return
            in_order(node.left)
            result.append(node.val)
            in_order(node.right)
        in_order(root)
        return result[k-1]
