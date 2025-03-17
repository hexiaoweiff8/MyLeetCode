from collections import defaultdict

class Solution(object):
    def sumOfPowers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ret = 0
        dp = [[defaultdict(int) for _ in range(k + 1)] for _ in range(n)]
        nums.sort()
        for i in range(n):
            dp[i][1][float('inf')] = 1
            for j in range(i):
                diff = abs(nums[i] - nums[j])
                for p in range(2, k + 1):
                    for v, cnt in dp[j][p - 1].items():
                        dp[i][p][min(diff, v)] = (dp[i][p][min(diff, v)] + cnt) % 1000000007
            for x, cnt in dp[i][k].items():
                ret = (ret + x * cnt % 1000000007) % 1000000007
        return ret