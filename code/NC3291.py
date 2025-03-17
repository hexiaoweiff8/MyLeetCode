class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        dp = [0] * (len(target) + 1)
        dp[0] = 1
        for word in words:
            for i in range(len(target), -1, -1):
                if i + len(word) > len(target):
                    continue
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] += dp[i]
                    dp[i + len(word)] %= 1000000007

        return dp[-1]