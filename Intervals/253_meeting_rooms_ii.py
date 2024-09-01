#!/usr/bin/env python3

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start_times = [i[0] for i in intervals]
        end_times = [i[1] for i in intervals]

        start_times.sort()
        end_times.sort()
        prev = 0
        rooms = 0

        for i in range(len(start_times)):
            if start_times[i] < end_times[prev]:
                rooms += 1
            else:
                prev += 1
        
        return rooms
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert solution.minMeetingRooms([[7,10],[2,4]]) == 1