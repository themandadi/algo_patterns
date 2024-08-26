#!/usr/bin/env python3

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    

if __name__ == "__main__":
    cycle = Solution()

    # assert cycle.hasCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4, ListNode(2))))))
    head = ListNode(1, ListNode(2, ListNode(1)))
    head.next = head
    assert cycle.hasCycle(head)
    assert not cycle.hasCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4)))))
