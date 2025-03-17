class Solution(object):
    def maximumPoints(self, edges, coins, k):
        """
        :type edges: List[List[int]]
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        for i, j in edges:
            if i not in dic:
                dic[i] = []
            dic[i].append(j)
            if j not in dic:
                dic[j] = []
            dic[j].append(i)

        def dfs(x, fa):
            s = [0] * 14
            for y in dic[x]:
                if y != fa:
                    fy = dfs(y, x)
                    for j, v in enumerate(fy):
                        s[j] += v
            for j in range(13):
                s[j] = max((coins[x] >> j) - k + s[j], (coins[x] >> (j + 1)) + s[j + 1])
            s[13] += (coins[x] >> 13) - k
            return s
        return dfs(0, -1)[0]