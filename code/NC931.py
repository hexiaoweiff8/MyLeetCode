class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cur = matrix[0]
        dp = [0] * len(cur)
        n = len(matrix)
        for index in range(1, n):
            for index2 in range(n):
                if index2 == 0:
                    dp[index2] = min(cur[index2], cur[index2 + 1])
                elif index2 == n - 1:
                    dp[index2] = min(cur[index2], cur[index2 - 1])
                elif 0 < index2 < n - 1:
                    dp[index2] = min(cur[index2 - 1], cur[index2], cur[index2 + 1])
                dp[index2] += matrix[index][index2]
            dp, cur = cur, dp
        return min(cur)


obj = Solution()
print(obj.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(obj.minFallingPathSum([[-19, 57], [-40, -5]]))
print(obj.minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))
print(obj.minFallingPathSum([[-84, -36, 2], [87, -79, 10], [42, 10, 63]]))
