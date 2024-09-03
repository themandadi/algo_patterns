#!/usr/bin/env python3

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(n):
            if n == len(nums) - 1:
                res.append(nums[:])
                return
            else:
                for i in range(n, len(nums)):
                    nums[n], nums[i] = nums[i], nums[n]
                    backtrack(n+1)
                    nums[n], nums[i] = nums[i], nums[n]
        res: List[List[int]] = []
        backtrack(0)

        return res
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
    assert solution.permute([0,1]) == [[0,1],[1,0]]
    assert solution.permute([1]) == [[1]]