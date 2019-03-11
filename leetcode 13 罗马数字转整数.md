### # leetcode 13 罗马数字转整数

```python
# 可能我对题目的描述有误解，在此并不多说，分享解法
# 判断后边的罗马数字和前边一个的关系， 如果前边小就对结果减去前边的值， 反之则加
# 比如 'CD' D > C
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
        }

        if not s:
            return 0

        res = 0
        pre = roma_map[s[0]]

        for ch in s[1:]:
            if roma_map[ch] > pre:
                res -= pre
            else:
                res += pre
            pre = roma_map[ch]
        res += pre
        
        return res
```

