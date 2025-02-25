#!/usr/bin/env python3

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        seen = {}

        for i, n in enumerate(nums2):

            while stack and stack[-1] < n:
                num = stack.pop()
                seen[num] = n
            
            stack.append(n)

        return [seen.get(n, -1) for n in nums1]
    

if __name__ == "__main__":
    temp = Solution()

    assert temp.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert temp.nextGreaterElement([2,4], [1,2,3,4]) == [3, -1]
        