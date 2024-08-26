#!/usr/bin/env python3

# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring of s such that every character in t (including duplicates) is included in the
# window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

from typing import List
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(t) > len(s):
            return ""

        if s == t:
            return s

        result: List[str] = []
        left, right = 0, len(s)
        l_t = len(t)
        k = 0
        new_right = 0

        while left < right and new_right < right:
            new_right = l_t + left + k
            curr_sub = s[left:new_right]
            all = True
            for c in t:
                if c not in curr_sub:
                    all = False
                    break
            if all:
                result.append(curr_sub)
                left += l_t
            else:
                k += 1
                left += l_t

        return min(result, key=len)
    
    def minWindow2(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        t_count = Counter(t)  # Count of all characters in t
        window_count = defaultdict(int)

        have, need = 0, len(t_count)
        left = 0
        result = float("inf"), None, None  # Length of result, start, end

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update result if this window is smaller
                if (right - left + 1) < result[0]:
                    result = (right - left + 1), left, right

                # Pop the leftmost character from the window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = result[1], result[2]
        return s[l:r + 1] if result[0] != float("inf") else ""
    

if __name__ == "__main__":
    min_win = Solution()

    assert min_win.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert min_win.minWindow(s="a", t="a") == "a"
    assert min_win.minWindow(s="a", t="aa") == ""
    assert min_win.minWindow(s="abc", t="b") == "bc"

    # Code that works for all test test cases:
    assert min_win.minWindow2(s="abc", t="b") == "b"