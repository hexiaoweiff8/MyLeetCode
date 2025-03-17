class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """

        def getMaxSum(nums, k):
            lenNums = len(nums)
            dp = [[0] * (k + 1) for _ in range(lenNums)]
            dp[0][1] = nums[0]
            dp[1][1] = max(nums[0], nums[1])
            for i in range(2, lenNums):
                for j in range(1, k + 1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + nums[i])
            return dp[lenNums - 1][k]

        lenSlices = len(slices)
        return max(getMaxSum(slices[0: lenSlices - 1], lenSlices // 3), getMaxSum(slices[1: lenSlices], lenSlices // 3))


obj = Solution()
print(obj.maxSizeSlices([1, 2, 3, 4, 5, 6]))
print(obj.maxSizeSlices([8, 9, 8, 6, 1, 1]))
