#!/usr/bin/env python3

# Given the head of a singly linked list, return true if it is a 
# palindrome or false otherwise.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            curr = node
            prev = None

            while curr is not None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        fast = head
        slow = head
        curr = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = reverse(slow)

        while rev and curr:
            if rev.val != curr.val:
                return False
            rev = rev.next
            curr = curr.next
        return True

    def is_palindrome_stack(self, head):
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head

        while curr and stack.pop() == curr.val:
            curr = curr.next

        return curr is None


