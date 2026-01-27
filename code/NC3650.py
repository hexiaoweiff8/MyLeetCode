import heapq


class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        for x, y, v in edges:
            g[x].append([y, v])
            g[y].append([x, v * 2])

        dis = [float('inf')] * n
        dis[0] = 0
        q = [(0, 0)]

        while q:
            d, x = heapq.heappop(q)
            if d > dis[x]:
                continue
            if x == n - 1:
                return d
            for y, v in g[x]:
                nDisV = dis[x] + v
                if dis[y] > nDisV:
                    dis[y] = nDisV
                    heapq.heappush(q, (nDisV, y))

        return -1