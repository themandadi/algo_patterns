# LINKED LIST #

A linked list is a linear data structure whose elements are not stored in contiguous memory locations, unlike arrays. This can be done because each element stored inside the linked list has a pointer to the next element.

Types Of Linked Lists

There are 4 different kinds of linked lists: singly linked list, doubly linked list, circular list, and doubly circular list. These can sound a little more complex than they truly are so let’s break each one down real quick.
Singly Linked List

A singly linked list is a linked list where each node only points to one node and the tail node points to null. This was represented in the picture above.
Circular Linked List

A circular linked list never ends, just like if you were to follow the line of a circle… it just keeps wrapping back onto itself. This type of linked list is simply a singly linked list where the tail, instead of pointing to null points back to the head node.

Doubly Linked List

A node in a singly linked list only has one pointer which points to the next node in the linked list. A node in a doubly linked list on the other hand has two pointers, one pointing to the next node and the other pointing to the previous node.

This allows you to traverse the linked list in both directions. The head in a doubly linked list will point to both null and the next node. The tail in a doubly linked list will point to null and the previous node.

Doubly Circular Linked List

A doubly circular linked list is a doubly linked list whose head’s previous node will be the tail instead of null. And the tail’s next node will be the head instead of null.

## Example Problems ##

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [Remove Linked List ELements](https://leetcode.com/problems/remove-linked-list-elements/)
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)