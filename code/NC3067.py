class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        n = len(edges) + 1
        dic = [[] for _ in range(n)]
        for edge in edges:
            dic[edge[0]].append([edge[1], edge[2]])
            dic[edge[1]].append([edge[0], edge[2]])

        def dfs(x, fa, s):
            cnt = 0 if s % signalSpeed else 1
            for y, t in dic[x]:
                if y == fa: continue
                cnt += dfs(y, x, s + t)
            return cnt

        ans = [0] * n
        for i, lst in enumerate(dic):
            if len(lst) == 1:
                continue
            s = 0
            for y, t in lst:
                cnt = dfs(y, i, t)
                ans[i] += cnt * s
                s += cnt
        return ans


obj = Solution()
print(obj.countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1))
