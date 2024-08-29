#!/usr/bin/env python3


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        left_s, right_s = 0, len(s)
        left_t, right_t = 0, len(t)

        while left_s < right_s and left_t < right_t:
            if s[left_s] == t[left_t]:
                left_s += 1
            left_t += 1

        return right_s - left_s == 0
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.isSubsequence(s="abc", t="ahbgdc")
    assert not solution.isSubsequence(s="axc", t="ahbgdc")