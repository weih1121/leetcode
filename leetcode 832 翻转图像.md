### leetcode 832 翻转图像

```python
# 解法非常容易说一下这里遇到的问题
# 在第一个for循环中想直接改变值来避免第二次循环， 结果未奏效
class Solution:
    def flipAndInvertImage(self, A):
        if not A:
            return A

        for i in A:
            start, end = 0, len(A[0]) - 1
            while start <= end:
                i[start], i[end] = i[end], i[start]
                start, end = start + 1, end - 1
        for index, val in enumerate(A):
            for i, value in enumerate(val):
                A[index][i] = 0 if A[index][i] else 1
        return A

```

```python
# python for循环通过迭代器实现，迭代器具有只读属性(循环过程对迭代器加锁)
# 可通过下标访问或者enumerate遍历实现此处通过下标进行解决
class Solution:
    def flipAndInvertImage(self, A):
        if not A:
            return A

        len_A = len(A)
        for i in range(len_A):
            start, end = 0, len_A - 1
            while start < end:
                A[i][start] = 0 if A[i][start] else 1
                A[i][end] = 0 if A[i][end] else 1
                A[i][start], A[i][end] = A[i][end], A[i][start]
                start, end = start + 1, end - 1
            if start == end:
                A[i][start] = 0 if A[i][start] else 1
        return A
```

```python 
# 通过异或运算优化if条件判断
class Solution:
    def flipAndInvertImage(self, A):
        if not A:
            return A

        len_A = len(A)
        for i in range(len_A):
            start, end = 0, len_A - 1
            while start < end:
                A[i][start] ^= 1
                A[i][end] ^= 1
                A[i][start], A[i][end] = A[i][end], A[i][start]
                start, end = start + 1, end - 1
            if start == end:
                A[i][start] ^= 1
        return A
```

```python
# 此题目也可以通过reverse函数或者切片操作来进行处理， 做法更加pythonic
class Solution:
    def flipAndInvertImage(self, A):
        return [[j ^ 1 for j in i[::-1]] for i in A]
```

