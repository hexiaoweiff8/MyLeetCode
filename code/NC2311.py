class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n, m = len(s), k.bit_length()
        if n < m:
            return n
        ans = m if int(s[-m:], 2) <= k else m - 1
        return ans + s[:-m].count("0")