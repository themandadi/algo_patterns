### MONOTONIC STACK ###

```
Monotonic stack is a stack with the guarantee of monotonicity for stack elements, which is more strictly limited than a normal stack. It requires that every element pushed onto the stack must be sorted (if the new element pushed does not meet the requirement, the previous elements will be popped out of the stack until the requirement is met before pushing the new element), forming a monotonic increasing or decreasing stack.

Monotonic stack is a relatively simple data structure. Compared with monotonic queue, it only performs push and pop operations on one end.
```

#### Example Problems: ####
- [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/)
- [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)