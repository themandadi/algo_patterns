#!/usr/bin/env python3

# Given an integer array nums, return the length of the longest strictly increasing subsequence.


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert solution.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert solution.lengthOfLIS([7,7,7,7,7,7,7]) == 1