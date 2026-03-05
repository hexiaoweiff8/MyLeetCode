class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] != str(i % 2):
                ans += 1

        return min(ans, n - ans)
