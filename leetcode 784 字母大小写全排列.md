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

```python
# 解法二 递归
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permutation(s, index, prefix):
            if index > len(s) - 1:
                return prefix

            tmp = []
            for p in prefix:
                if s[index].isdigit():
                    tmp.append(p + s[index])
                else:
                    tmp.append(p + s[index].lower())
                    tmp.append(p + s[index].upper())
            res = permutation(s, index + 1, tmp)
            return res
        return permutation(S, 0, [''])
```

