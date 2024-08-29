#!/usr/bin/env python3

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.:

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) / 2
        dp = set([0])

        for num in nums:
            temp_set = set()
            for i in dp:
                if i + num == target:
                    return True
                temp_set.add(i + num)
            dp.update(temp_set)
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.canPartition([1, 5, 11, 5])
    assert not solution.canPartition([1, 2, 3, 5])