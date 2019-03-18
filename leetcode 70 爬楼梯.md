### # leetcode 70 爬楼梯

```python
# 解法一 自顶向下的思考方法，自底向上的实现方式，采用递归便是自顶向下的实现方式
# 举例: 假设最后剩一个台阶则有一种走法，就是剩n - 1个台阶的走法，剩两个台阶则走法就是n - 2个台阶的走法
# 此解法存在冗余，比如变量过多
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        res, pre, cur = 0, 1, 1
        num = 2

        while num <= n:
            res, pre = pre + cur, cur
            cur, num = res, num + 1
        return res
```

```python
# 简单优化之后
# 此种解法时间复杂度 O(n) 但是做到这里就结束了吗？ 显然没有....
class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur, n = 1, 1, n - 1

        while n:
            pre, cur, n = cur, pre + cur, n - 1
        
        return cur
```

