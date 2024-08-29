#!/usr/bin/env python3

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy: int = prices[0]
        max_profit: int = 0

        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            max_profit = max(max_profit, prices[i] - buy)

        return max_profit
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0