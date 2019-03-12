### # leetcode 401 二进制手表

```python
# 主要思路在于通过一位灯亮的结果 递推2个灯亮的结果，并递推更多
# 题目隐含条件 小时数不大于11 我也是通过观察返回结果发现的
# 注：python3提交 不通过没有默认的set数据结构
# 注：答案顺序不对 仍然算错 第一种解法无法通过
class Solution:
    def readBinaryWatch(self, num: int):
        if num == 0:
            return ['0:00']
        
        res, tmp = [('', '')], []
        mins = ['1', '2', '4', '8', '16', '32']
        hours = ['1', '2', '4', '8']

        for i in range(num):
            for tup in res:
                for min_ in mins:
                    if not min_ in tup[1]:
                        tmp.append((tup[0], tup[1] + '-' + min_))
                for hour in hours:
                    if not hour in tup[0]:
                        tmp.append((tup[0] + '-' + hour, tup[1]))
            res, tmp = tmp, []

        m, h = 0, 0
        for tup in res:
            for ch in tup[1].split('-'):
                if not ch == '-' and ch:
                    m += int(ch)
                h = m // 60
                m = m % 60

            for ch in tup[0].split('-'):
                if not ch == '-' and ch:
                    h += int(ch)
            if h < 12:
                tmp.append((str(h) if h else '0') + ':' + (str(m) if m >= 10 else ('0' + str(m))))
            m, h = 0, 0

        return set(tmp)
```

