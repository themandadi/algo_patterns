#!/usr/bin/env python3

# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            second.next = first
            first.next = second.next
            curr = curr.next.next

        return dummy.next