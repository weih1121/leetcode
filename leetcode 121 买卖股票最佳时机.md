### leetcode 121 买卖股票最佳时机

```python
# 通过将所有结果列出来 判断是否有符合交易的情况，如果有从中取出最大值
# 此算法超时
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        pre = 0
        for index, i in enumerate(prices):
            for j in prices[index + 1:]:
                pre = j - i if j - i > pre else pre
        return pre
```

```python
# 通过分析可知，若要获取最大利益，需要从数组中获取一个极小值和一个极大值， 且极小值需要在极大值左侧
# 算法思路: 通过遍历记录之前出现的最小值，并且记录满足条件的差值(收益值)
# 此题解法最基础是通过一个数组记录每个位置和最小值的差值，最后遍历那个记录数组获取最大值(此为最原始的动态规划解法)，在此处通过两个变量记录差值和最小值，优化空间
# dp方程: max(前一天最大差值， 几天和前i天最小值的最大差值)
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        pre_min, res =prices[0], 0
        for i in prices:
            pre_min = pre_min if pre_min < i else i
            res = res if res > i - pre_min else i - pre_min
        return res
```

```python
# 此解法与上述解法思路相同，只是使用min函数和if三目运算符差别，经过提交测试，此种解法运行效率略低于if三目运算符
# 效率差 在40ms左右
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        pre_min, res = prices[0], 0
        for i in prices:
            pre_min = min(pre_min, i)
            res = max(res, i - pre_min)
        return res
```

