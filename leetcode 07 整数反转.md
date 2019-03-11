### #3 leetcode 07 整数反转

```python
# 解法一: 取数字最后一位 * 10 + 计算出来的数 判断大小关系
class Solution:
    def reverse(self, x: int) -> int:
        b = 0
        if x < 0:
            b, x = 1, abs(x)
        mod, res = 0, 0
        while x:
            x, mod = x // 10, x % 10
            res = res * 10 + mod
            if res > 2147483648:
                return 0
        if b == 1:
            res = -res
        return res
```

```python
# 解法二: 取符号位 将数字转化为字符串 利用reverse函数 之后转成int判断关系
class Solution:
    def reverse(self, x: int) -> int:
        b, res = '', ''
        if x < 0:
            b = '-'
            x = str(abs(x))
        else:
            x = str(x)
        
        for i in reversed(x):
            res += i
        if int(res) > 2**31:
            return 0
        return int(res) if b == '' else int(b + res)
```

