#/usr/bin/env python3

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        element = 0

        for num in nums:

            if count == 0:
                element = num
            
            if num == element:
                count += 1
            else:
                count -= 1
        
        return element


if __name__ == "__main__":
    solution = Solution()

    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
            