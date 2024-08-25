#!/usr/local/bin python3

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

from typing import Dict, List


class Solution:

    def __repr__(self) -> str:
        return "Solution()"

    def findMaxLength(self, nums: List[int]) -> int:
        
        max_sub: int = 0
        count: int = 0
        prefix: Dict[int, int] = {0: -1}

        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1

            if count in prefix:
                max_sub = max(max_sub, i - prefix[count])
            else:
                prefix[count] = i


        return max_sub
    
if __name__ == "__main__":
    find_max = Solution()
    print(find_max)
    assert find_max.findMaxLength([0,1]) == 2
    assert find_max.findMaxLength([0,1,0]) == 2
