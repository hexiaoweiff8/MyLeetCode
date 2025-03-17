import collections

N = 100000
is_prime = [True] * N
is_prime[1] = False
for i in range(2, N):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False


class Solution(object):
    def countPaths(self, n, edges):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            seen.append(node)
            for child in graph[node]:
                if child == parent:
                    continue
                if not is_prime[child]:
                    dfs(child, node)
        ret = 0
        count = [0] * (n + 1)
        for i in range(1, n + 1):
            if not is_prime[i]:
                continue
            cur = 0
            for j in graph[i]:
                if is_prime[j]:
                    continue
                if count[j] == 0:
                    seen = []
                    dfs(j, 0)
                    for node in seen:
                        count[node] = len(seen)
                ret += cur * count[j]
                cur += count[j]
            ret += cur
        return ret


obj = Solution()
print(obj.countPaths(n=5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]]))
