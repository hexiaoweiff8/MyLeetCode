class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges)
        graph = {}
        for (i, j) in edges:
            dic = graph.get(i, {"to": []})
            dic["to"].append(j)
            graph[i] = dic
