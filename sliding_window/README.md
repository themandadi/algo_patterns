# SLIDING WINDOW #

Concept of Sliding Window
The idea behind the sliding window technique is to create a "window" that moves (or slides) across the data structure, allowing you to examine a portion of the data at any given time without repeatedly processing the entire dataset. The window size can be fixed or dynamic depending on the problem.

How Sliding Window Works
Initialization:

Start by defining the window's boundaries. For instance, you might have two pointers: one at the beginning (left) and one at the end (right) of the window. Initially, the window might be empty or contain a small subset of the data.
Slide the Window:

Move the window across the data structure by adjusting the pointers (usually by moving the right pointer to the right). As you do this, adjust the window by including or excluding elements as needed.
Update State:

After each movement, update any necessary variables or data structures that keep track of the current state of the window (e.g., current sum, max, min).
Check Condition:

Often, after each slide, you’ll check whether the current state meets the problem’s conditions. If it does, you might record the result, or continue sliding to find other valid windows.

Time and Space complexity of the sliding window technique:

Time Complexity:
The time complexity of the sliding window technique is usually linear or close to linear, O(n), where n is the size of the input data structure (e.g., array or string). This is because you process each element once as the window slides through the data.
Space Complexity:
The space complexity of the sliding window technique is generally constant, O(1), because you’re maintaining a fixed-size window and a few additional variables to perform calculations or store intermediate results. The amount of extra memory used doesn’t grow with the input size; it remains constant regardless of the input size.

## Example Problems ##

- [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)