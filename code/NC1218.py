from collections import defaultdict


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = defaultdict(int)
        for i in arr:
            dp[i] = dp[i - difference] + 1
        return max(dp.values())
