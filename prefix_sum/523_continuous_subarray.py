#!/usr/bin/env python3

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

#     its length is at least two, and
#     the sum of the elements of the subarray is a multiple of k.

# Note that:

#     A subarray is a contiguous part of the array.
#     An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

from typing import List, Dict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        result = False

        if len(nums) <= 1:
            return result

        prefix_sum: Dict = {0 : -1}
        remainder = 0

        for i, n in enumerate(nums):
            remainder += n
            remainder %= k

            if remainder not in prefix_sum:
                prefix_sum[remainder] = i
            elif i - prefix_sum[remainder] >= 2:
                return True

        return result

if __name__ == "__main__":
    check_sub = Solution()

    assert check_sub.checkSubarraySum(nums=[23,2,4,6,7], k=6)
    assert check_sub.checkSubarraySum(nums=[23,2,6,4,7], k=6)
    assert not check_sub.checkSubarraySum(nums=[23,2,6,4,7], k=13)
