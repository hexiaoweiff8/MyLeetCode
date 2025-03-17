class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # t是分钟数
        def check(t):
            # 标记火焰的位置
            f = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 1]
            onFire = set(f)
            def spreadFire():
                # 火势bfs
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    # 处理上下左右
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if m > x >= 0 and 0 <= y < n and (x, y) not in onFire:
                            f.append((x, y))
                            onFire.add((x, y))

            # 如果有时间并且可以扩散火势
            while t and f:
                spreadFire()
                t -= 1
            if (0, 0) in onFire:
                return False

            # 计算人的bfs
            q = [(0, 0)]
            visHistory = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) in onFire:
                        continue
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if m > x >= 0 and 0 <= y < n and grid[x][y] == 0 and (x, y) not in onFire and (x, y) not in visHistory:
                            if x == m - 1 and y == n - 1:
                                # 到达终点
                                return True
                            q.append((x, y))
                            visHistory.add((x, y))
                # 推演火势
                spreadFire()
            return False
        # 二分法
        left = -1
        right = m * n + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left if left < m * n else 10 ** 9