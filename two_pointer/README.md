# TWO POINTER #

Two Pointer algorithm are typically used for searching pair elements in the sorted array. The two Pointer algorithm is an efficient method to search pairs in sorted array. Because Time Complexity of searching pair elements in array using Naive approach(To process one element per loop) depends on their size. But, Two pointer algorithm is able to process two elements per loop.
How to use

    Each pointer starts at the beginning index and end index of the data structure.
    Iterate until the met condition or both pointers are met.

The Big-O Time Complexity is O(N) because we need to find all elements in worst case. In this situation, pointer_1 always stops starting points and pointer_2 moves until meets pointer_1.
The Big-O Space Complexity is O(1) because we don’t need any data structure which can store elements. We just use two pointers that indicate the address of memory.

## Example Problems ##

- [Two Sum II - input sorted array](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/)
- [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)
- [3Sum](https://leetcode.com/problems/3sum/)
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [Move Zeros](https://leetcode.com/problems/move-zeroes/)
- [Is Sequence](https://leetcode.com/problems/is-subsequence/)
- [Squares Of Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)