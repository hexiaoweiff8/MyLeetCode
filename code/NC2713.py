class Solution(object):
    def maxIncreasingCells(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。
        从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。
        你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。
        请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。
        返回一个表示可访问单元格最大数量的整数。
        """
        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if mat[x][y] == 0:
                return 1
            mat[x][y] = 0
            res = max(dfs(x - 1, y), dfs(x + 1, y), dfs(x, y - 1), dfs(x, y + 1))
            mat[x][y] = 1
            return res + 1
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    return dfs(i, j)

        return 0