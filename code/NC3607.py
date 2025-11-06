from sortedcontainers import SortedList


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(c + 1)
        for u, v in connections:
            uf.union(u, v)
        st = [SortedList() for _ in range(c + 1)]
        for i in range(1, c + 1):
            st[uf.find(i)].add(i)
        ans = []
        for a, x in queries:
            root = uf.find(x)
            if a == 1:
                if x in st[root]:
                    ans.append(x)
                elif len(st[root]):
                    ans.append(st[root][0])
                else:
                    ans.append(-1)
            else:
                st[root].discard(x)
        return ans


obj = Solution()
print(obj.processQueries(3, [], [[1,1],[2,1],[1,1]]))
