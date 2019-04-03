### # leetcode 5 最长回文子串

~~~python
# 解法一： 暴力法通过判断每个子串是否是回文串，并记录回文串的长度和位置，最后将子串返回
# 暴力法虽好但是通不过
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return ""

        res_tup = (0, 0)

        for index, val in enumerate(s):
            i, e = 0, index
            while i < e:
                res = self.is_back_str(s, i, e)
                if res:
                    if (e - i) > res_tup[1] - res_tup[0]:
                        res_tup = (i, e)
                i += 1
        return s[res_tup[0]:res_tup[1] + 1]

    def is_back_str(self, tar, s, e):
        if e <= s:
            return False

        while s < e:
            if not tar[s] == tar[e]:
                return False

            s, e = s + 1, e - 1
        return True
~~~

