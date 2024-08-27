#!/usr/bin/env python3

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter.

# Do not modify the linked list.


from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        
        return
    
if __name__ == "__main__":
    cycle = Solution()

    # assert cycle.hasCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4, ListNode(2))))))
    # head = ListNode(1, ListNode(2, ListNode(1)))
    # head.next = head
    # assert cycle.hasCycle(head) == ListNode(1)
    assert not cycle.hasCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4)))))