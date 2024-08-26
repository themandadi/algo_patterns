#!/usr/bin/env python3

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray,
# return 0 instead.

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target: return 0

        count, left = 0, 0
        result = len(nums)

        for right, n in enumerate(nums):
            count += n
            while count >= target:
                count -= nums[left]
                result = min(result, right - left + 1)
                left += 1

        return result
    

if __name__ == "__main__":
    min_sub = Solution()

    assert min_sub.minSubArrayLen(nums=[2,3,1,2,4,3], target=7) == 2
    assert min_sub.minSubArrayLen(nums=[1,4,4], target=4) == 1
    assert min_sub.minSubArrayLen(nums=[1,1,1,1,1,1,1,1], target=11) == 0