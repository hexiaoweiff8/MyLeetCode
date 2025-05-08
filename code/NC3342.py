from heapq import heappop, heappush


class Solution(object):
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while True:
            d, i, j = heappop(pq)
            if i == n - 1 and j == m - 1:
                return d
            if d > dist[i][j]:
                continue
            toggle_time = (i + j) % 2 + 1
            for a, b in dirs:
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < m:
                    t = max(dist[i][j], moveTime[x][y]) + toggle_time
                    if t < dist[x][y]:
                        dist[x][y] = t
                        heappush(pq, (t, x, y))
