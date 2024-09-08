#!/usr/bin/env python3

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root and root.val == targetSum and (root.left or root.right) and not (root.left and root.right):
            return []
        output = []
        def dfs(node, target, level):
            if not node:
                return

            if target - node.val == 0:
                if not node.right and not node.left:
                    level.append(node.val)
                    output.append(level)
                    return

            dfs(node.left, target - node.val, level + [node.val])
            dfs(node.right, target - node.val, level + [node.val])
        
        dfs(root, targetSum, [])
        return output