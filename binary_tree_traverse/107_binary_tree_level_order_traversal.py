#!/usr/bin/env python3

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        queue = deque([root])

        if not root:
            return result

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result[::-1]
    