class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        lenArr = len(arr)
        dp = [0] * (lenArr + 1)
        for index in range(1, lenArr + 1):
            mx = 0
            for index2 in range(index, max(0, index - k), -1):
                mx = max(mx, arr[index2 - 1])
                dp[index] = max(dp[index], dp[index2 - 1] + mx * (index - index2 + 1))
        return dp[lenArr]


obj = Solution()
print(obj.maxSumAfterPartitioning( [1,15,7,9,2,5,10], 3))