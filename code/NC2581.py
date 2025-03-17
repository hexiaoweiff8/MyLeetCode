import collections


class Solution(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        s = {(x, y) for x, y in guesses}
        self.ans = self.cnt0 = 0
        def dfs(x, fa):
            for y in graph[x]:
                if y != fa:
                    self.cnt0 += (x, y) in s
                    dfs(y, x)
        dfs(0, -1)

        def reroot(x, fa, cnt):
            self.ans += cnt >= k
            for y in graph[x]:
                if y != fa:
                    reroot(y, x, cnt - ((x, y) in s) + ((y, x) in s))
        reroot(0, -1, self.cnt0)
        return self.ans