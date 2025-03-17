class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen = len(s)
        dp = [[0] * strLen for _ in range(strLen)]
        maxLen = 0
        end = start = 0
        for r in range(strLen):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = 1
                    if r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        start = l
                        end = r
        return s[start: end + 1]

    def longestPalindrome2(self, s):
        strLen = len(s)
        dp = [[0] * strLen for _ in range(strLen)]
        maxLen = 0
        end = start = 0
        for r in range(strLen):
            for l in range(r):
                if s[l] == s[r] and (r - 1 <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = 1
                    if r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        start = l
                        end = r
        return s[start: end + 1]