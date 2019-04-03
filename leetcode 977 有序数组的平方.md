### leetcode 977 有序数组的平方

```python
# 思路首先想到对数组中每个值求平方再进行一次排序，这样做的时间复杂度是排序的时间复杂度，
# 再想到原数组有序，O(n)的想法便产生了，只需要从分界点(大于0)的两侧进行比较然后平方保存即可
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        pos, len_arr, ret = 0, len(A), []
        for i in range(len_arr):
            if A[i] >= 0:
                pos = i
                break
        index, post_index = pos - 1, pos

        while index >= 0 or post_index < len_arr:
            if index >= 0:												# 左半部分存在
                if post_index < len_arr and -A[index] <= A[post_index]:	# 右半部分存在且左边值小于右边值得绝对值
                    ret.append(A[index] ** 2)
                    index -= 1
                elif post_index == len_arr:								# 右半部分已经都计算完毕
                    ret.append((A[index] ** 2))
                    index -= 1
            if post_index < len_arr:
                if index >= 0 and -A[index] >= A[post_index]:
                    ret.append(A[post_index] ** 2)
                    post_index += 1
                elif index < 0:
                    ret.append(A[post_index] ** 2)
                    post_index += 1
        return ret
```

```python
# 当然比较pythonic的做法是如下这样
# 这个代码的执行效率比上一个要高一些，个人觉得是因为语言实现层面对结果影响较大
# 从时间复杂度方面分析第一种解法时间复杂度明显优于此
class Solution:
    def sortedSquares(self, A):
        return sorted([x ** 2 for x in A])
```

