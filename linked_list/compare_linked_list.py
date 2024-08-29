#!/usr/bin/env python3

from typing import Any


def compare_linked_list(node1: Any, node2: Any):

    while node1 is not None and node2 is not None:
        assert node1.val == node2.val
        node1 = node1.next
        node2 = node2.next

    assert node1 is None and node2 is None
