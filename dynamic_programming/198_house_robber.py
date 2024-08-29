#!/usr/bin/env python3

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        prev, curr = nums[0], max(nums[0], nums[1])

        for n in range(2, len(nums)):
            prev, curr = curr, max(curr, prev + nums[n])
        
        return curr
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([0]) == 0
    assert solution.rob([2,7,9,3,1]) == 12

        