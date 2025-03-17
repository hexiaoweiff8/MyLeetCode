class Solution(object):
    def countKConstraintSubstrings(self, s, k, queries):
        """
        :type s: str
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            if s[i] == 'a':
                dp[i + 1] = dp[i] + 1
            else:
                dp[i + 1] = dp[i]
        res = []
        for start, end in queries:
            if dp[end + 1] - dp[start] >= k:
                res.append(1)
            else:
                res.append(0)
        return res