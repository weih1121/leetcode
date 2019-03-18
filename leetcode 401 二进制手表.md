### # leetcode 401 二进制手表

提交一个反面教材 

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

```python
# 解法二 此解法并非最优解 但是可以ac
# 思路和解法一类似 在通过前一次的结果递推后一次结果时 增加了剪枝但是仍然会存在重复
# 此处去重借助collections包中的counter
# 对于结果排序问题，通过自定义排序的lambda sorted函数
# 虽然可以ac但是过程过于艰辛 但是仍有收获
from collections import Counter
class Solution:
    def readBinaryWatch(self, num: int):
        if num == 0:
            return ['0:00']
        
        res, tmp = [('', '')], []
        mins = ['1', '2', '4', '8', '16', '32']
        hours = ['1', '2', '4', '8']

        for _ in range(num):
            for tup in res:
                for min_ in mins:
                    if not tup[1] or (len(tup[1]) and tup[1].split('-')[-1] < min_):
                        tmp.append((tup[0], tup[1] + '-' + min_))
                for hour in hours:
                    if not tup[0] or (len(tup[0]) and tup[0].split('-')[-1] < hour):
                        if tup[1].split('-')[-1] < hour:
                            tmp.append((tup[0] + '-' + hour, tup[1]))
            res, tmp = tmp, []

        res = list(Counter(res).keys())

        for r in res:
            m, h = 0, 0
            for ch in r[0].split('-'):
                if ch and (ch != '-'):
                    h += int(ch)
            if h >= 12:
                continue

            for ch in r[1].split('-'):
                if ch != '-' and ch:
                    m += int(ch) 
            
            if m >= 60:
                continue
            
            tmp.append((str(h) if h else '0') + ':' + (str(m) if m >= 10 else ('0' + str(m))))

        return sorted(tmp, key=lambda x: int(x.split(':')[0]) * 100 + int(x.split(':')[1]))
```

