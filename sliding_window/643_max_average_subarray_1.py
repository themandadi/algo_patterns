#!/usr/bin/env python3

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and
# return this value. Any answer with a calculation error less than 10-5 will be accepted.

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        curr_sum: int = sum(nums[:k])
        max_sum: int = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k
    

if __name__ == "__main__":
    find_max = Solution()

    assert find_max.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4) == 12.7500
    assert find_max.findMaxAverage(nums=[5], k=1) == 5.00000
    assert find_max.findMaxAverage(nums=[4,0,4,3,3], k=5) == 2.80000