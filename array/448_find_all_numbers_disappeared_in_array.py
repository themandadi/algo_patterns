#!/usr/bin/env python3

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        output: List[int] = []

        for num in nums:
            index = abs(num)-1
            nums[index] = -1 * abs(nums[index])

        for i, n in enumerate(nums):
            if n > 0:
                output.append(i+1)

        return output
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
    assert solution.findDisappearedNumbers([1,1]) == [2]
    assert solution.findDisappearedNumbers([4,5,6,7,8,2,3,1]) == []
