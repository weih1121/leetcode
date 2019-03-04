# #3 leetcode 03 无重复字符的最长子串

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            m = 0
            return m
        hash_map = {}
        len_arr = [1 for i in range(len(s))]
        m = 1
        for index, val in enumerate(s):
            if not val in hash_map:
                if index != 0:
                    len_arr[index] = len_arr[index - 1] + 1
            else:
                if (hash_map[s[index - 1]] - len_arr[index - 1] + 1) <= hash_map[val]:
                    len_arr[index] = hash_map[s[index - 1]] - hash_map[val] + 1
                else:
                    len_arr[index] = len_arr[index - 1] + 1
            m = len_arr[index] if len_arr[index] >= m else m
            hash_map[val] = index
        return m
```

