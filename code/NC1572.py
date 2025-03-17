class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        matLen = len(mat)
        sumVal, x1, y, x2 = 0, 0, 0, matLen - 1
        while x1 < matLen:
            sumVal += mat[x1][y] + mat[x2][y]
            x1 += 1
            y += 1
            x2 -= 1
        if matLen % 2 == 1:
            sumVal -= mat[matLen // 2][matLen // 2]
        return sumVal


obj = Solution()
print(obj.diagonalSum(mat=[[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]))
print(obj.diagonalSum(mat=[[1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1]]))
