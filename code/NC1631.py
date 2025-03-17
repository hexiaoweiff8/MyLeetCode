class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # m, n = len(heights), len(heights[0])
        # dp = [[999999999] * n for _ in range(m)]
        # dp[0][0] = heights[0][0]
        # for i in range(m):
        #     for j in range(n):
        #         gap1, gap2 = None, None
        #         if i > 0:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j])
        #             gap1 = abs(heights[i][j] - heights[i - 1][j])
        #         if j > 0:
        #             dp[i][j] = min(dp[i][j - 1], dp[i][j])
        #             gap2 = abs(heights[i][j] - heights[i][j - 1])
        #         dp[i][j] = max(dp[i][j], min(gap1 if gap1 else 0, gap2 if gap2 else 0))
        #
        # return dp[-1][-1]
        closeMap = set()
        def dfs(x, y, fromX, fromY):
            if (x, y) in closeMap:
                return
            closeMap.add((x, y))
            if x == len(heights) - 1 and y == len(heights[0]) - 1:
                return




obj = Solution()
# print(obj.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
# print(obj.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(obj.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
