#!/usr/bin/env python3

# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

# Implement the TwoSum class:

#     TwoSum() Initializes the TwoSum object, with an empty array initially.
#     void add(int number) Adds number to the data structure.
#     boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


class TwoSum:

    def __init__(self):
        self.nums = []

    def __repr__(self) -> str:
        return "TwoSum()"

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:

        left = 0
        right = len(self.nums) - 1

        self.nums.sort()

        while left < right:
            total = self.nums[left] + self.nums[right]

            if value == total:
                return True
            elif total > value:
                right -= 1
            else:
                left += 1

        return False


if __name__ == "__main__":
    two_sum = TwoSum()
    two_sum.add(1)
    two_sum.add(2)
    assert not two_sum.find(1)
