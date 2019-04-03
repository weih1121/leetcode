### leetcode 53 最大自序和

~~~python
# 解法一 穷举 i 表示取数组中元素的个数， j表示数组开始的位置
# 此解法由于枚举效率过低 超出时间限制
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None
        lmax, larr = -9e32, len(nums)

        for i in range(1, larr + 1):
            j = 0
            while i + j <= larr:
                tmp = sum(nums[j: i + j])
                lmax = tmp if tmp > lmax else lmax
                j += 1
        return lmax
~~~

```python
# 解法二 动态规划 arr[i]表示 以数组中第i个元素为终点的最大子序和
# 半成品 仍然可以优化
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None

        pre, cur, res = -1e32, None, -1e32
        for i, val in enumerate(nums):
            cur = val if val > pre + val else pre + val
            pre, res = cur, res if res > cur else cur
        return res
```

```python
# 优化版一 经过测试发现enumarate效率较低
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None

        pre_max = ret = nums[0]
        nums = nums[1:] 			# 这一行代码可以使测试用例节约内存至少300m 相较于循环处切片方法
        for i in nums:
            pre_max = i if i > i + pre_max else i + pre_max
            ret = ret if ret > pre_max else pre_max
        return ret
```

```python
# 优化版二 使用列表的__len__()函数获取列表元素长度，通过索引操作数组避免切片 可以减少内存占用
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None
        def get_max(nums, st, end):
            pre_max = ret = nums[0]

            for i in range(st, end):
                pre_max = nums[i] if nums[i] > nums[i] + pre_max else nums[i] + pre_max
                ret = ret if ret > pre_max else pre_max
            return ret

        return get_max(nums, 1, nums.__len__())
```

```python
# 分治策略
# 最大值可能在数组左边 可能在数组右边 可能跨越数组中央
# 跨越中央时需计算最大前缀和最大后缀
def maxSubArray(nums, start, end):
    if not nums:
        return None

    if start == end:
        return nums[start]

    mid = (start + end) // 2
    left = maxSubArray(nums, start, mid)	# 左边最大值
    right = maxSubArray(nums, mid + 1, end)	# 右边最大值
    pre, post = nums[mid], nums[mid + 1]	# pre前缀 post后缀

    max_pre_post = pre
    for i in range(mid - 1, start - 1, -1):
        pre += nums[i]
        max_pre_post = max_pre_post if max_pre_post > pre else pre
    
    pre, max_pre_post = max_pre_post, post
    for i in range(mid + 2, end + 1):
        post += nums[i]
        max_pre_post = max_pre_post if max_pre_post > post else post
    post = max_pre_post

    return max(left, right, pre + post)		# 最大值即为 左中右中最大的
```

