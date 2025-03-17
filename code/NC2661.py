class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        row = [0] * m
        col = [0] * n
        dic = {}
        for i in range(m):
            for j in range(n):
                dic[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            x, y = dic[arr[i]]
            row[x] += 1
            col[y] += 1
            if row[x] == n or col[y] == m:
                return i

        return -1


obj = Solution()
print(obj.firstCompleteIndex(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]]))
print(obj.firstCompleteIndex(arr=[2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
print(obj.firstCompleteIndex(arr=[1, 4, 5, 2, 6, 3], mat=[[4, 3, 5], [1, 2, 6]]))
