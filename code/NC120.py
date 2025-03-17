class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp, dp2 = [], []
        level = 0
        for tri in triangle:
            for _ in range(len(dp2) - len(dp) + 1):
                dp.append(0)
            level += 1
            for index, node in enumerate(tri):
                if index == 0:
                    dp[index] = (dp2[index] if dp2 else 0) + node
                elif index == level - 1:
                    dp[index] = dp2[index - 1] + node
                else:
                    dp[index] = min(dp2[index - 1], dp2[index]) + node
            dp, dp2 = dp2, dp
        return min(dp2) if dp2 else triangle[0][0]


obj = Solution()
print(obj.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(obj.minimumTotal(triangle=[[-10]]))
