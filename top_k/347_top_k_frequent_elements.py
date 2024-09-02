#!/usr/bin/env python3

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List, Dict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cache: Dict[int, int] = {}
        result = []

        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        
        result = [[i, v] for i,v in cache.items()]
        result.sort(key=lambda x: x[1], reverse=True)

        return [r[0] for r in result[:k]]


if __name__ == "__main__":
    solution = Solution()

    assert solution.topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]