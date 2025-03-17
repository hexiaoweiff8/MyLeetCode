class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 前缀和+动态规划
        # 处理前缀和
        numsLen = len(nums)
        preSums = [0.0] * (numsLen + 1)
        for index in range(1, numsLen + 1):
            preSums[index] = preSums[index - 1] + nums[index - 1]
        dp = [[0.0] * (k + 1) for _ in range(numsLen + 1)]
        for index in range(1, numsLen + 1):
            dp[index][1] = preSums[index] / index

        for i in range(2, k + 1):
            for j in range(i, numsLen + 1):
                for x in range(i - 1, j):
                    dp[j][i] = max(dp[j][i], dp[x][i - 1] + (preSums[j] - preSums[x]) / (j - x))
        return dp[numsLen][k]


obj = Solution()
print(obj.largestSumOfAverages([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 4))
