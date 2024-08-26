#!/usr/bin/env python3

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(self.square(n))

        while slow != fast and fast != 1:
            slow = self.square(slow)
            fast = self.square(self.square(fast))

        return fast == 1

    def square(self, n):

        result = 0

        while n > 0:
            remainder = n % 10
            result += remainder * remainder
            n //= 10
        return result


if __name__ == "__main__":
    happy = Solution()

    assert happy.isHappy(19)
    assert not happy.isHappy(2)
