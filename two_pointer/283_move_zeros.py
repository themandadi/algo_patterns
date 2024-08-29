#!/usr/bin/env python3


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        left: int = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert solution.moveZeroes([0,0]) == [0,0]