#!/usr/bin/env python3

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_steps = nums[0]
        steps = nums[0]

        for n in range(1, len(nums)):
            max_steps = max(max_steps, nums[n] + n)
            steps -= 1

            if steps < 0:
                return False
            elif steps == 0:
                steps = max_steps - n
        
        return True
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.canJump([2,3,1,1,4])
    assert not solution.canJump([3,2,1,0,4])