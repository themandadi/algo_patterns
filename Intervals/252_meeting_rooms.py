#!/usr/bin/env python3

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x: x[1])

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    assert not solution.canAttendMeetings([[0,30],[5,10],[15,20]])
    assert solution.canAttendMeetings([[7,10],[2,4]])