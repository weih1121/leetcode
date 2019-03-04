# leetcode 02 两数相加

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []
        i = 0
        tag = 0
        while l1 or l2:
            lhs, rhs = l1.val if l1 else 0, l2.val if l2 else 0
            res.append((lhs + rhs+ tag) % 10)
            tag = 1 if lhs + rhs + tag >= 10 else 0
            l1, l2, i = l1.next if l1 else None, l2.next if l2 else None , i + 1
        if tag == 1:
            res.append(1)
        return res
```

