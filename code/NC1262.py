class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]
        for index, num in enumerate(nums):
            a = dp[0] + num
            b = dp[1] + num
            c = dp[2] + num
            dp[a % 3] = max(dp[a % 3], a)
            dp[b % 3] = max(dp[b % 3], b)
            dp[c % 3] = max(dp[c % 3], c)

        return dp[0]


obj = Solution()
print(obj.maxSumDivThree([3,6,5,1,8]))
print(obj.maxSumDivThree([4]))
print(obj.maxSumDivThree([1,2,3,4,4]))