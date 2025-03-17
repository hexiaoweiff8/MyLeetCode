class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 1
        cur = 1
        for i in range(len(s) - 1):
            if ord(s[i + 1]) == ord(s[i]) + 1:
                cur += 1
            else:
                res = max(cur, res)
                cur = 1
        return max(cur, res)