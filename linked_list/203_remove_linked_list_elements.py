#!/usr/bin/env python3

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

from typing import Optional

from compare_linked_list import compare_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        curr = node

        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return node.next


if __name__ == "__main__":
    solution = Solution()

    node = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    node1 = solution.removeElements(node, 6)
    node2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    assert compare_linked_list(node1, node2) is None