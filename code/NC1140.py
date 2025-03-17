class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        pilesLen = len(piles)
        sum = 0
#         dp = [[0] * (pilesLen + 1) for _ in range(pilesLen)]
#         for index in range(pilesLen - 1, -1, -1):
#             sum += piles[index]
#             for m in range(1, pilesLen + 1):
#                 if index + 2 * m >= pilesLen:
#                     # 本回合能够到的极限
#                     dp[index][m] = sum
#                 else:
#                     for index2 in range(1, 2 * m + 1):
#                         dp[index][m] = max(dp[index][m], sum - dp[index + index2][max(m, index2)])
#
#         return dp[0][1]
#
#
# obj = Solution()
# print(obj.stoneGameII([2, 7, 9, 4, 4]))
# print(obj.stoneGameII([1, 2, 3, 4, 5, 100]))
        dp = [[0] * (pilesLen + 1) for _ in range(pilesLen)]