#!/usr/bin/env python3

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = float('-inf')

        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area


if __name__ == "__main__":
    max_area = Solution()

    assert max_area.maxArea(height=[1,8,6,2,5,4,8,3,7]) == 49
    assert max_area.maxArea(height=[1,1]) == 1
