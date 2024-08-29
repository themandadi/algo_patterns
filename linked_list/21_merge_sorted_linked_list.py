#!/usr/bin/env python3

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

from typing import Optional

from compare_linked_list import compare_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        res = head

        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        
        head.next = list1 or list2

        return res.next
    

if __name__ == "__main__":
    solution = Solution()

    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(5)))
    node = solution.mergeTwoLists(node1, node2)
    ans = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

    assert compare_linked_list(node, ans) is None