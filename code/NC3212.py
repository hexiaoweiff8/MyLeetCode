class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        preSum = [[[0, 0] for _ in range(n)] for _ in range(m)]
        # 计算每行的x和y的和的前缀和
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    preSum[i][j][0] += 1
                elif grid[i][j] == 'Y':
                    preSum[i][j][1] += 1
                if j > 0:
                    preSum[i][j][0] += preSum[i][j - 1][0]
                    preSum[i][j][1] += preSum[i][j - 1][1]
        # 计算每个子矩阵的x和y的和的前缀和
        for i in range(1, m):
            for j in range(n):
                preSum[i][j][0] += preSum[i - 1][j][0]
                preSum[i][j][1] += preSum[i - 1][j][1]

        # 计算x数量=y输量的子矩阵数量
        res = 0
        for i in range(m):
            for j in range(n):
                if preSum[i][j][0] == preSum[i][j][1] and preSum[i][j][0] > 0:
                    res += 1

        return res


obj = Solution()
print(obj.numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
