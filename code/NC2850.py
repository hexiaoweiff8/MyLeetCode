from itertools import permutations


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # 遍历获取所有0的位置和所有大于1的位置
        zeros = []
        upOnes = []
        ret = 99999999
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 1:
                    zeros.extend([(i, j)] * (grid[i][j] - 1))
                elif grid[i][j] == 0:
                    upOnes.append((i, j))
        for upOnes2 in permutations(upOnes):
            total = 0
            for (i, j), (i2, j2) in zip(upOnes2, zeros):
                total += abs(i - i2) + abs(j - j2)
            ret = min(ret, total)
        return ret