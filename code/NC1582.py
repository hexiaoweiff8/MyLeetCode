class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n, m = len(mat), len(mat[0])
        # 对角线遍历 并记录每行/列的1的个数
        rowCount = [0] * n
        colCount = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    res += 1
        return res
