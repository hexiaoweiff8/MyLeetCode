from heapq import heappop, heappush


class Solution(object):
    def minimumTime(self, n, edges, disappear):
        graph = [[] for _ in range(n)]
        ret = [999999999] * n
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        dist = [float('inf')] * n
        dist[0] = 0
        stack = [(0, 0)]
        while stack:
            dx, x = heappop(stack)
            if dx > dist[x]:
                continue
            for y, length in graph[x]:
                if dist[y] > dist[x] + length and dist[x] + length < disappear[y]:
                    dist[y] = dist[x] + length
                    heappush(stack, (dist[y], y))
        return [a if a < b else -1 for a, b in zip(dist, disappear)]


obj = Solution()
print(obj.minimumTime(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5]))
