class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 计算matrix中1的数量
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j] if i > 0 else 0

        # 求最大的子矩阵面积
        ans = 0
        for i in range(n):
            # 对matrix[i][j] 排序
            matrix[i].sort()
            # 求最大的子矩阵面积
            for j in range(m):
                ans = max(ans, matrix[i][j] * (m - j))

        return ans
