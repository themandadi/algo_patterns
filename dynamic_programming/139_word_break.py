#!/usr/bin/env python3

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [True] + [False] * len(s)

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]
    

if __name__ == "__main__":
    solution = Solution()

    assert solution.wordBreak("leetcode", ["leet","code"])
    assert solution.wordBreak("applepenapple", ["apple","pen"])
    assert not solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"])