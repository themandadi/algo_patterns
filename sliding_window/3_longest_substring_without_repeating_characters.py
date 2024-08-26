#!/usr/bin/env python3

# Given a string s, find the length of the longest substring without repeating characters.
from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        seen: Dict = {}
        left: int = 0
        result: int = 1

        for right in range(len(s)):
            if s[right] not in seen or seen[s[right]] < left:
                result = max(result, right - left + 1)
            else:
                left = seen[s[right]] + 1
            seen[s[right]] = right
        
        return result
    

if __name__ == "__main__":
    ls = Solution()

    assert ls.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert ls.lengthOfLongestSubstring(s="bbbbb") == 1
    assert ls.lengthOfLongestSubstring(s="pwwkew") == 3
    assert ls.lengthOfLongestSubstring(s="") == 0