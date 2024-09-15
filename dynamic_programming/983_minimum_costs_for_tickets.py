#!/usr/bin/env python3

# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        last_traverl_day = days[-1]
        dp_cost = [  0 for _ in range(last_traverl_day+1)]
    
        for day_i in range(1, last_traverl_day+1):
            if day_i not in days:
                dp_cost[day_i] = dp_cost[day_i - 1]
            else:
                dp_cost[day_i] = min(   dp_cost[ day_i - 1 ]  + costs[0],
                                        dp_cost[ max(day_i - 7, 0) ]  + costs[1],
                                        dp_cost[ max(day_i - 30, 0) ] + costs[2])
        
        return dp_cost[last_traverl_day]
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
    assert solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17