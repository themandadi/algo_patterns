#!/usr/bin/env python3

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        old_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        if old_color == color:
            return image

        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()
            if image[r][c] == old_color:
                image[r][c] = color

                if r-1 >= 0:
                    queue.append((r-1, c))
                if r+1 < rows:
                    queue.append((r+1, c))
                if c - 1 >= 0:
                    queue.append((r, c-1))
                if c+1 < cols:
                    queue.append((r, c+1))
        return image
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert solution.floodFill([[0,0,0],[0,0,0]], 1, 1, 0) == [[0,0,0],[0,0,0]]