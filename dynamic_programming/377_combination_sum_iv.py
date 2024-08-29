#!/usr/bin/env python3

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        
        return dp[target]
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.combinationSum4([1, 2, 3], 4) == 7
    assert solution.combinationSum4([9], 3) == 0