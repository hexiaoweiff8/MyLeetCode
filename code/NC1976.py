import collections
from heapq import heappop, heappush


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        mod = 10 ** 9 + 7
        dis = [0] + [float('inf')] * (n - 1)
        ways = [1] + [0] * (n - 1)

        q = [[0, 0]]
        while q:
            u, d = heappop(q)
            if u > dis[d]:
                continue
            for v, w in graph[d]:
                if u + w < dis[v]:
                    dis[v] = u + w
                    ways[v] = ways[d]
                    heappush(q, [u + w, v])
                elif u + w == dis[v]:
                    ways[v] = (ways[v] + ways[d]) % mod

        return ways[-1]
