### leetcode 771 宝石与石头

```python
# helloworld 题目
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(J)
        ret = 0
        for i in S:
            ret = ret + 1 if i in j else ret
        return ret
```



