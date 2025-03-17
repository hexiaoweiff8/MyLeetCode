class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        ans = (float("inf"), -1)
        mp = [[float("inf")] * n for _ in range(n)]
        for fr, to, w, in edges:
            mp[to][fr], mp[fr][to] = w, w
        for i in range(n):
            mp[i][i] = 0
            for j in range(n):
                for k in range(n):
                    mp[j][k] = min(mp[j][k], mp[j][i] + mp[i][k])
        for i in range(n):
            cnt = sum(mp[i][j] <= distanceThreshold for j in range(n))
            if cnt <= ans[0]:
                ans = (cnt, i)
        return ans[1]




obj = Solution()
print(obj.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
