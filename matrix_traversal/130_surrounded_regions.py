#!/usr/bin/env python3

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
        return board
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    assert solution.solve([["X"]]) == [["X"]]