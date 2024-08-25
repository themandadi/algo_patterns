#!/usr/bin/env python3

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List, Set

class Solution:
    def threeSum(self, nums: List[int]) -> Set[tuple[int]]:

        nums.sort()
        nums_len: int = len(nums)
        result: Set = set()

        for i in range(nums_len-2):
            left = i+1
            right = nums_len - 1
            
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                elif target > 0:
                    right -= 1
                else:
                    left += 1

        return result
    

if __name__ == "__main__":
    three_sum = Solution()

    assert three_sum.threeSum(nums=[-1,0,1,2,-1,-4]) == {(-1,0,1), (-1,-1,2)}
    assert three_sum.threeSum(nums=[0,1,1]) == set()
    assert three_sum.threeSum(nums=[0,0,0]) == {(0,0,0)}
