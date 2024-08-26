#!/usr/bin/env python3

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
if __name__ == "__main__":
    max_sub = Solution()

    assert max_sub.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_sub.maxSubArray([1]) == 1
    assert max_sub.maxSubArray([5,4,-1,7,8]) == 23
        