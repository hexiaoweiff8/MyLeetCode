from collections import defaultdict


class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = defaultdict(list)
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        g2 = defaultdict(list)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        def dfs(g, node, u, k):
            if k < 0:
                return 0
            if k == 0:
                return 1
            ret = 1
            for v in g[node]:
                if v != u:
                    ret += dfs(g, v, node, k - 1)
            return ret

        mx = 0
        for i in range(m):
            mx = max(mx, dfs(g2, i, -1, k - 1))
        ans = [0] * n
        for i in range(n):
            ans[i] = dfs(g1, i, -1, k) + mx
        return ans


obj = Solution()
print(obj.maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                         edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k=2))
