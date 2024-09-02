#!/usr/bin/env python3

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                top = 0
                bottom = n
                while top < bottom:
                    mid = (top + bottom) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        top = mid + 1
                    else:
                        bottom = mid
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
    assert not solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) 