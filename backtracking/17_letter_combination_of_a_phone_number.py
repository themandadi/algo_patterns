#!/usr/bin/env python3

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        result = []

        if not digits:
            return result

        registry = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrack(start, comb):

            if len(comb) == len(digits):
                result.append(comb[:])
                return
            else:            
                for i in registry[digits[start]]:
                    backtrack(start+1, comb + i)
        
        backtrack(0, "")

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert solution.letterCombinations("") == []
    assert solution.letterCombinations("2") == ["a","b","c"]
