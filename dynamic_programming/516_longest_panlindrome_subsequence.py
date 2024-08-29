#!/usr/bin/env python3

# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        len_s = len(s)
        if not s or s == s[::-1]:
            return len_s

        dp = [[1] * len_s for _ in range(len_s)]

        for i in range(len_s):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and j + 1 < i:
                    dp[j][i] = dp[j+1][i-1] + 2
                elif s[i] == s[j] and j + 1 == i:
                    dp[j][i] = 2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])

        return dp[0][len_s-1]
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.longestPalindromeSubseq("bbbab") == 4
    assert solution.longestPalindromeSubseq("cbbd") == 2