### # leetcode 784 字母大小写全排列

```python
# 回溯法 通过前一个状态的结果递推后续的序列
# e.g. 'abs' 第一次res = ['a', 'A'] 下一次迭代以上一个res为基础添加字符'b'
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']

        res, tmp = [''], []

        for ch in S:
            if  '0' <= ch <= '9':
                for item in res:
                    tmp.append(item + ch)
            else:
                for item in res:
                    tmp.append(item + ch.lower())
                    tmp.append(item + ch.upper())
            res, tmp = tmp, []
        return res
```

