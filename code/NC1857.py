import collections


class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """

        def dfs(index):
            # 从index开始遍历
            visited[index] = True
            for gList in g[index]:
                for v in gList:
                    if visited[v]:
                        return -1
                    if dfs(v) == -1:
                        return -1
                    for i in range(26):
                        colorsDic[index][i] = max(colorsDic[index][i], colorsDic[v][i])
            return
        n = len(colors)
        g = [[] for _ in range(n)]
        colorsDic = collections.defaultdict(list)
        visited = [False] * n
        for u, v in edges:
            g[u].append(v)
            # 检查环
            if u in g[v]:
                return -1

