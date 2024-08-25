#!/usr/bin/env python3

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import Dict, List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum: Dict[int, int] = {0: 1}
        count: int = 0
        ans: int = 0

        for i in range(len(nums)):
            count += nums[i]
            if count - k in prefix_sum:
                ans += prefix_sum[count - k]
            
            if count in prefix_sum:
                prefix_sum[count] += 1
            else:
                prefix_sum[count] = 1

        return ans


if __name__ == "__main__":
    sub_sum = Solution()

    assert sub_sum.subarraySum(nums=[1,1,1], k=2) == 2
    assert sub_sum.subarraySum(nums=[1,2,3], k=3) == 2