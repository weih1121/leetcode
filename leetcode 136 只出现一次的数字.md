### leetcode 136 只出现一次的数字

```python
# 解法一:
# 使用哈希表

# 解法二:
# 数组中只有一个数不同，则其他数异或的结果为0,0与其他数异或的结果为另一个数
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]
        for n in range(1, len(nums)):
            ret = ret ^ nums[n]
        return ret
    
# 解法三:
# 使用集合求出唯一数的2倍值，减去数组中数的和，便是那个唯一数
```

