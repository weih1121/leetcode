### # leetcode 09 回文数

```python
# 解法一: 输入数小于0 直接false，否则将正整数反转 判断是否相等
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        if x < 0:
            return False
        
        res, mod = 0, 0
        while x:
            x, mod = x // 10, x % 10
            res = res * 10 + mod
        return a == res
```

```python
# 解法二: 若是正数通过转化为反转串转成int 判断是否与原数同
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = x
        x = int(str(x)[::-1])
        return x == a
```

