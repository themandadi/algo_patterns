#!/usr/bin/env python3

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = [root.val]

        def in_order(node):

            if not node:
                return 0
            
            left =  max(0, in_order(node.left))
            right = max(0, in_order(node.right))

            max_path[0] = max(max_path[0], left + node.val + right)
            return node.val + max(left, right)
            
        in_order(root)
        return max_path[0]