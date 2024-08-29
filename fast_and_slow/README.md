# FAST AND SLOW (TORTOISE & HARE) #

This technique is commonly known as the ‘Fast & Slow Pointer’ or ‘Tortoise and Hare Algorithm,’ and it essentially embodies Floyd’s Cycle Detection Algorithm.
The primary purpose of this technique is to determine the presence of a ‘CYCLE’ in a linked list or array
The algorithm involves the use of ‘Slow’ and ‘Fast’ pointers. During each iteration, the slow pointer typically advances by one step, while the fast pointer advances by two steps.
If there is no cycle, the fast pointer eventually reaches a null value in a linked list. In such cases, the slow pointer indicates the middle item in the list.
If there is a cycle, the fast and the slow pointer meet at a point.
The pivotal part of this point is where the cycle starts. To determine this, one pointer (usually the slow pointer) is reset to the start of the linked list,
while the other pointer (fast pointer) remains at the meeting point. Both pointers then move at the same pace, and the next meeting point they encounter is the start of the cycle.

## Example Problems ##

- [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [Happy Number](https://leetcode.com/problems/happy-number/)
