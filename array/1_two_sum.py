#!/usr/bin/env python3

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


from typing import Dict, List


# time: O(n) | space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen: Dict[int, int] = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [i, seen[diff]]
            seen[n] = i

        return []

if __name__ == "__main__":
    two_sum = Solution()
    assert two_sum.twoSum(nums=[2,7,11,15], target=9) == [1, 0]
    assert two_sum.twoSum(nums=[3,2,4], target=6) == [2, 1]
    assert two_sum.twoSum(nums=[3,3], target=6) == [1, 0]