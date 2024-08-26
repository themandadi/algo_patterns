#!/usr/bin/env python3

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        return slow
    
    def findDuplicate2(self, nums: List[int]) -> int:
        for num in nums:
            curr = abs(num)

            if nums[curr] < 0:
                return curr
            nums[curr] = -nums[curr]
        return
        

if __name__ == "__main__":
    find_dup = Solution()

    assert find_dup.findDuplicate([1,3,4,2,2]) == 2
    assert find_dup.findDuplicate([3,1,3,4,2]) == 3
    assert find_dup.findDuplicate([3,3,3,3,3]) == 3