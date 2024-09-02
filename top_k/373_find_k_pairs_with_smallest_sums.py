#!/usr/bin/env python3

# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

from typing import List, Dict


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        cache: Dict[int, List[int]] = {}

        for num1 in nums1:
            for num2 in nums2:
                s = num1 + num2
                cache[s] = cache.get(s, [])
                cache[s].append([num1, num2])

        result = []
        for pairs in cache.values():
            result.extend(pairs)
        result.sort(key=lambda x: x[0] + x[1])

        return result[:k]
    

if __name__ == "__main__":
    solution = Solution()

    solution.kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    solution.kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]