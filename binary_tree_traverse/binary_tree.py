#!/usr/bin/env python3


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def pre_order_recursive(node):
    # NLR = Node, Left, Right
    if not node:
        return
    
    # recursive code:
    print(node.val, end=" ")
    pre_order_recursive(node.left)
    pre_order_recursive(node.right)


def pre_order_iterative(node):
    stack = [node]
    output = []

    while stack:
        n = stack.pop()
        if n:
            output.append(n.val)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    print(output)

def in_order():
    # LNR: Left, Node, Right
    ...


def post_order():
    # LRN: Left, Right, Node
    ...


if __name__ == "__main__":
    head = Node(1, (Node(2, Node(4), Node(5))), Node(3, Node(6)))
    pre_order_recursive(head)
    pre_order_iterative(head)
