class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 遍历获取箱子位置和玩家位置
        rowCount = len(grid)
        colCount = len(grid[0])
        sx, sy, bx, by = None, None, None, None
        for y in range(rowCount):
            for x in range(colCount):
                if grid[y][x] == "S":
                    sx = x
                    sy = y
                if grid[y][x] == "B":
                    bx = x
                    by = y

        def ok(x, y):
            return 0 <= x < colCount and 0 <= y < rowCount and grid[y][x] != "#"

        d = [0, -1, 0, 1, 0]

        dp = [[9999999] * (rowCount * colCount) for _ in range(rowCount * colCount)]
        dp[sy * colCount + sx][by * colCount + bx] = 0
        q = [(sy * colCount + sx, by * colCount + bx)]
        while q:
            q1 = []
            while q:
                s1, b1 = q.pop()
                sy1, sx1 = s1 // colCount, s1 % colCount
                by1, bx1 = b1 // colCount, b1 % colCount
                if grid[by1][bx1] == "T":
                    return dp[s1][b1]
                for i in range(4):
                    sx2, sy2 = sx1 + d[i], sy1 + d[i + 1]
                    s2 = sy2 * colCount + sx2
                    if not ok(sx2, sy2):
                        continue
                    if sx2 == bx1 and sy2 == by1:
                        bx2, by2 = bx1 + d[i], by1 + d[i + 1]
                        b2 = by2 * colCount + bx2
                        if not ok(bx2, by2) or dp[s2][b2] <= dp[s1][b1] + 1:
                            continue
                        dp[s2][b2] = dp[s1][b1] + 1
                        q1.append((s2, b2))
                    else:
                        if dp[s2][b1] <= dp[s1][b1]:
                            continue
                        dp[s2][b1] = dp[s1][b1]
                        q.append((s2, b1))
            q, q1 = q1, q
        return -1


obj = Solution()
print(obj.minPushBox(grid=[["#", ".", ".", "#", "#", "#", "#", "#"],
                           ["#", ".", ".", "T", "#", ".", ".", "#"],
                           ["#", ".", ".", ".", "#", "B", ".", "#"],
                           ["#", ".", ".", ".", ".", ".", ".", "#"],
                           ["#", ".", ".", ".", "#", ".", "S", "#"],
                           ["#", ".", ".", "#", "#", "#", "#", "#"]]
                     ))
