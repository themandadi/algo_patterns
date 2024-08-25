#!/usr/bin/env python3

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        right: int = len(nums) - 1
        left: int = 0

        while left < right:
            total = nums[left] + nums[right]

            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1

        return []
    

if __name__ == "__main__":
    two_sum = Solution()
    assert two_sum.twoSum(nums=[2,7,11,15], target=9) == [1, 2]
    assert two_sum.twoSum(nums=[2,3,4], target=6) == [1, 3]
    assert two_sum.twoSum(nums=[-1, 0], target=-1) == [1, 2]