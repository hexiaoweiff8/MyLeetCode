from collections import defaultdict


class Solution:
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        # 变更: 使用类型注解，变量名改为 graph1 和 graph2
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def dfs(g, node, u, index):
            ret = 1 if index % 2 == 0 else 0
            for v in g[node]:
                if v != u:
                    ret += dfs(g, v, node, index + 1)
            return ret

        mx = 0
        n, m = len(graph1), len(graph2)
        a = dfs(graph2, 0, -1, 1)
        mx = max(mx, a, n - a)
        ans = [0] * m
        ans[0] = dfs(graph1, 0, -1, 0)

        # 变更: 修改 dfs2 函数的参数顺序
        def dfs2(node, u, g):
            for v in g[node]:
                if v != u:
                    ans[v] = m - ans[node]
                    dfs2(v, node, g)

        # 变更: 直接调用 dfs2，移除多余的变量赋值
        dfs2(0, -1, graph1)

        # 变更: 直接返回结果，移除多余的变量赋值
        return [i + mx for i in ans]