#!/usr/bin/env python3

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count: int = 0
        prev: int = 0
        intervals.sort(key=lambda x: x[1])

        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                count += 1
            else:
                prev = i
        
        return count
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert solution.eraseOverlapIntervals([[1,2],[2,3]]) == 0