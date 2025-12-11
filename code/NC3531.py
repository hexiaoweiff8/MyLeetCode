class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        ans = 0
        row_min = [n + 1] * (n + 1)
        col_min = [n + 1] * (n + 1)
        row_max = [0] * (n + 1)
        col_max = [0] * (n + 1)

        for x, y in buildings:
            if x < row_min[y]:
                row_min[y] = x
            if x > row_max[y]:
                row_max[y] = x
            if y < col_min[x]:
                col_min[x] = y
            if y > col_max[x]:
                col_max[x] = y

        for x, y in buildings:
            if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
                ans += 1
        return ans
obj = Solution()
print(obj.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]))
