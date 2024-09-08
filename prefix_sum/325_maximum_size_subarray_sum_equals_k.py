#!/usr/bin/env python3

# Given an integer array nums and an integer k, return the maximum length of a 
# subarray
#  that sums to k. If there is not one, return 0 instead.

 

# Example 1:

# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        if sum(nums) == k:
            return len(nums)

        prefix_map = {0 : -1}
        prefix_sum = 0
        max_sub = 0

        for i, n in enumerate(nums):
            prefix_sum += n

            if prefix_sum - k in prefix_map:
                max_sub = max(max_sub, i - prefix_map[prefix_sum - k])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_sub
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSubArrayLen([1,-1,5,-2,3], 3) == 4
    assert solution.maxSubArrayLen([-2,-1,2,1], 1) == 2