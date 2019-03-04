# leetcode 01 两数和

解法一:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums, 0):
            if (target - num) in nums[index + 1: ]:
                i = nums[index + 1:].index(target - num) + 1 + index
                return [index, i]
        return []
# 耗时988ms
# 内存13.6mb
```

解法二:

```python
# 使用双端队列实现  想通过双端队列减少列表切片操作 所占用的额外内存大小 结果差距不大
from collections import deque
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = deque(nums)
        i = 0
        lhs = d.popleft()
        while d:
            if (target - lhs) in d:
                index = d.index(target - lhs) + i + 1
                return [i, index]
            i += 1
            lhs = d.popleft()
        return []
# 耗时 968ms
# 内存 13.5mb
```

解法三:

```python
# 使用hashmap 减少查找时间
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            lhs = target - num
            if lhs in hashmap:
                return [hashmap[lhs], index]
            hashmap[num] = index
        return []
     
```

