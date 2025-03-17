class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edgeDic, edgeCount = [[False] * n for _ in range(n)], [0] * n
        ret = 999999999999999999
        for edge in edges:
            u, v = edge[0] - 1, edge[1] - 1
            edgeDic[u][v] = edgeDic[v][u] = True
            edgeCount[u] += 1
            edgeCount[v] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if edgeDic[i][j]:
                    for k in range(j + 1, n):
                        if edgeDic[i][k] and edgeDic[j][k]:
                            ret = min(ret, edgeCount[i] + edgeCount[j] + edgeCount[k] - 6)
        if ret == 999999999999999999:
            return -1
        return ret


obj = Solution()
print(obj.minTrioDegree(n=6, edges=[[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]))
print(obj.minTrioDegree(n=7, edges=[[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]))
