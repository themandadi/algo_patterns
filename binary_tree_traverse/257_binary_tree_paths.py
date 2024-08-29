#!/usr/bin/env python3

# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.


from typing import Optional, List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:  
        output = []

        def dfs(root, path):
            if root is None:
                return
            
            if path:
                path += "->" + str(root.val)
            else:
                path = str(root.val)
            
            if root.left is None and root.right is None:
                output.append(path)

            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, "")
        return output