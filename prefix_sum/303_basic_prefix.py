#!/usr/bin/env python3

# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pf = [0] * (len(nums) +1)

        for i in range(len(nums)):
            self.pf[i+1] = self.pf[i] + nums[i]

    def __repr__(self) -> str:
        return f"NumArray(nums: {self.nums})"

    def sumRange(self, left: int, right: int) -> int:
        return self.pf[right+1] - self.pf[left]


if __name__ == "__main__":

    num_arr = NumArray(nums=[-2,0,3,-5,2,-1])
    print(num_arr, end=" -> This is from dunder defination.")
    assert num_arr.sumRange(2, 5) == -1
    assert num_arr.sumRange(0, 2) ==  1
    assert num_arr.sumRange(0, 5) == -3
