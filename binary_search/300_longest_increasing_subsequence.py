#!/usr/bin/env python3

# Given an integer array nums, return the length of the longest strictly increasing subsequence.


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        res: List[int] = []

        def binary_search(res, n):

            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2

                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        
        return len(res)
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert solution.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert solution.lengthOfLIS([7,7,7,7,7,7,7]) == 1