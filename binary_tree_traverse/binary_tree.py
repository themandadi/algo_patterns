#!/usr/bin/env python3


from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def in_order_recurssive(node):
    # Left Node Right
    if not node:
        return
    
    in_order_recurssive(node.left)
    print(node.val, end=" ")
    in_order_recurssive(node.right)


def in_order_iterative(node):
    stack = []
    output = []

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        output.append(node.val)
        node = node.right

    print(output)


def pre_order_recursive(node):

    if not node:
        return

    print(node.val, end=" ")
    pre_order_recursive(node.left)
    pre_order_recursive(node.right)


def pre_order_iterative(node):

    stack = [node]
    output = []

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    print(output)


def post_order_recursive(node):

    if not node:
        return

    post_order_recursive(node.left)
    post_order_recursive(node.right)
    print(node.val, end=" ")


def post_order_iterative(node):

    stack = [node]
    output = []

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    print(output[::-1])


def level_order_traversal(node):

    queue = deque([node])
    output = []

    while queue:

        node = queue.popleft()
        if node:
            output.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(output[::-1])


if __name__ == "__main__":
    head = Node(1, (Node(2, Node(4), Node(5))), Node(3, Node(6)))
    pre_order_recursive(head)
    pre_order_iterative(head)
    in_order_recurssive(head)
    in_order_iterative(head)
    post_order_recursive(head)
    post_order_iterative(head)
    level_order_traversal(head)