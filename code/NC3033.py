class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        dic = {}
        maxCol = [-1] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    dic[(i, j)] = 0
                else:
                    maxCol[j] = max(maxCol[j], matrix[i][j])

        for i, j in dic:
            matrix[i][j] = maxCol[j]
        return matrix