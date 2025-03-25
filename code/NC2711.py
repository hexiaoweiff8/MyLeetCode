class Solution(object):
    def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                left_up = set()
                right_down = set()
                for k in range(i - 1, -1, -1):
                    if k >= 0 and j - (i - k) >= 0:
                        left_up.add(grid[k][j - (i - k)])
                    else:
                        break
                for k in range(i + 1, m):
                    if k < m and j + (k - i) < n:
                        right_down.add(grid[k][j + (k - i)])
                    else:
                        break
                res[i][j] = abs(len(left_up) - len(right_down))

        return res


obj = Solution()
print(obj.differenceOfDistinctValues(grid=[[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
