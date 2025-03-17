class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        ret = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    ret = max(ret, dp[i][j])

        return ret * ret


