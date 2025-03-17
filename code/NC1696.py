class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = [0]
        for i in range(1, len(nums)):
            if q[0] < i - k:
                q.pop(0)
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return dp[-1]

        # def dfs(index):
        #     if index >= len(nums):
        #         return 0
        #     lst = []
        #     for i in range(1, k + 1):
        #         if index + i < len(nums):
        #             lst.append(nums[index + i] + dfs(index + i))
        #     if lst:
        #         return max(lst)
        #     return 0
        #
        # return dfs(0) + nums[0]


obj = Solution()
print(obj.maxResult([1, -1, -2, 4, -7, 3], 2))
# print(obj.maxResult([10, -5, -2, 4, 0, 3], 3))
# print(obj.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))
