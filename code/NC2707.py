class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])

        return dp[-1]


obj = Solution()
print(obj.minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
print(obj.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))
