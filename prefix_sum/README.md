### PREFIX SUM ###

```A prefix sum array, also known as a cumulative sum array, is a derived array that stores the cumulative sum of elements in a given array. Each element in the prefix sum array represents the sum of all elements up to that index in the original array. It acts as a precursor to answering queries related to cumulative sums, allowing for fast and efficient computations. It also reduces time complexity giving us a way out of TLE. ```

```python
def construct_prefix_sum_array(arr):
  n = len(arr)
  prefix_sum = [0] * n
  prefix_sum[0] = arr[0]
  for i in range(1, n):
  prefix_sum[i] = prefix_sum[i — 1] + arr[i]
  return prefix_sum
```

- [303. Range Sum Query Immutable]( https://leetcode.com/problems/range-sum-query-immutable/description/)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/description/)
- [560. Subarray Sum Quals K](https://leetcode.com/problems/subarray-sum-equals-k/)