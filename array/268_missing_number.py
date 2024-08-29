#!/usr/bin/env python3

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n_sum:int = 0
        e_sum:int = 0
        nums.append(0)

        for i, n in enumerate(nums):
            e_sum += i
            n_sum += n

        return e_sum - n_sum


if __name__ == "__main__":
    solution = Solution()

    assert solution.missingNumber([3,0,1]) == 2
    assert solution.missingNumber([0,1]) == 2
    assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8