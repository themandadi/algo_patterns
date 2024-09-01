#!/usr/bin/env python3

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = 0
        intervals.sort(key=lambda x: x[0])

        while prev < len(intervals)-1:
            if intervals[prev][1] >= intervals[prev+1][0]:
                intervals[prev][1] = max(intervals[prev][1], intervals[prev+1][1])
                del intervals[prev+1]
            else:
                prev += 1

        return intervals
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert solution.merge([[1,4],[4,5]]) == [[1,5]]