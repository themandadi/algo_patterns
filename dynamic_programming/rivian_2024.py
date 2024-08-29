#!/usr/bin/env python3

# For a staircase of size 1-n, a frog can jump forward [1, 2, n] or backward [-1, -2, -n-1],
# Given array of frog jumps [1, -4, -2, 3] find a minimum starting step to start so that a frog
# doesn't fall off.

from typing import List


def stairCounter(jumps: List[int]) -> int:

    current_position = 0
    min_position = 0

    for jump in jumps:
        current_position += jump
        min_position = min(min_position, current_position)

    # The frog needs to start at a position such that the lowest position it reaches is step 1
    return 1 - min_position


if __name__ == "__main__":

    assert stairCounter([1, -4, -2, 2]) == 6
    assert stairCounter([5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 1
    assert stairCounter([2, -3, 1, 4, -1, -2]) == 2
    assert stairCounter([1, -1, 1, -1, 1, -1, 1, -1]) == 1

    
