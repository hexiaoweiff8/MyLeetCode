import collections


class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        restricted = set(restricted)
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        stack = [0]
        count = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                count += 1
                for nei in graph[node]:
                    if nei not in restricted:
                        stack.append(nei)
        return count