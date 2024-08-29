#!/usr/bin/env python3

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            if len(nums) <= 2:
                return max(nums)
            prev = nums[0]
            curr = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr, prev = max(nums[i] + prev, curr), curr

            return curr
        
        return max(helper(nums[1:]), helper(nums[:-1]))
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([1, 2, 3]) == 3