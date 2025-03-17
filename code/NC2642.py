import heapq


class Graph(object):
    def __init__(self, n, edges):
        self.graph = [[] for _ in range(n)]
        for x, y, cost in edges:
            self.graph[x].append([y, cost])

    def addEdge(self, edge):
        self.graph[edge[0]].append([edge[1], edge[2]])

    def shortestPath(self, node1, node2):
        dist = [float("inf")] * len(self.graph)
        dist[node1] = 0
        q = [[0, node1]]
        while q:
            cost, x = heapq.heappop(q)
            if x == node2:
                return cost
            for y, c in self.graph[x]:
                if dist[y] > cost + c:
                    dist[y] = cost + c
                    heapq.heappush(q, [dist[y], y])
        return -1


# Your Graph object will be instantiated and called as such:
obj = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(obj.shortestPath(3, 2))
print(obj.shortestPath(0, 3))
print(obj.addEdge([1, 3, 4]))
print(obj.shortestPath(0, 3))
