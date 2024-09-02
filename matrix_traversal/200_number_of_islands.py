#!/usr/bin/env python3

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(grid, r, c):

            if r<0 or r >=len(grid) or c <0 or c>=len(grid[0]) or grid[r][c] != "1":
                return
            
            grid[r][c] = "#"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    count += 1
        
        return count


if __name__ == "__main__":
    solution = Solution()

    assert solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
    assert solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3