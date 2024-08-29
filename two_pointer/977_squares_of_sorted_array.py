#!/usr/bin/env python3

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1
        result = [0] * (right + 1)

        for i in reversed(range(right+1)):
            s = nums[left]
            l = nums[right]

            if abs(s) > abs(l):
                result[i] = s * s
                left += 1
            else:
                result[i] = l * l
                right -= 1
        
        return result
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]