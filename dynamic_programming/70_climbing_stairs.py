#!/usr/bin/env python3

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0, 1]

        for i in range(n):
            steps[0], steps[1] = steps[1], steps[0] + steps[1]

        return steps[1]
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3