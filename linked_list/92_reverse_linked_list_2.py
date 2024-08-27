#!/usr/bin/env python3

# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two pointer approach.
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next

        for _ in range(right - left):
            next = curr.next
            curr.next, next.next, prev.next = next.next, prev.next, next
        
        return dummy.next
    

if __name__ == "__main__":
    rev = Solution()

    # [1,2,3,4,5] == [1, 4, 3, 2, 5]
    # assert rev.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4) == ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
