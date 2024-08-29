#!/usr/bin/env python3

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import Set, List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups: Set = set()

        for num in nums:
            if num in dups:
                return True
            dups.add(num)
        
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.containsDuplicate([1,2,3,1])
    assert not solution.containsDuplicate([1,2,3,4])
    assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])