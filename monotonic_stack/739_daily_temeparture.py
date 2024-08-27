#!/usr/bin/env python3

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
# is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        len_t = len(temperatures)
        ans = [0] * len_t
        stack = []

        for i, t in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < t:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)

        return ans
    

if __name__ == "__main__":
    temp = Solution()

    assert temp.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert temp.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert temp.dailyTemperatures([30,60,90]) == [1,1,0]
