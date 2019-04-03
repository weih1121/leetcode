### leetcode 709 大写字符串转换为小写字符串

```python
# ascll 小写字母 在97~122之间
# 大写字母在65~97范围
class Solution:
    def toLowerCase(self, str: str) -> str:
        ret = ''
        for ch in str:
            ch = chr(ord(ch) + 32) if 65 <= ord(ch) <= 90 else ch
            ret += ch
        return ret
```



```python
# 利用python内置的转换函数，效率差20ms左右
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
```

