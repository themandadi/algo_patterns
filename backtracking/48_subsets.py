#!/usr/bin/env python3

# Given an integer array nums of unique elements, return all possible subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, path):
            result.append(path)

            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])
        
        result: List[List[int]] = []
        backtrack(0, [])

        return result
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert solution.subsets([0]) == [[], [0]]