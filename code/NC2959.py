class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # 查找所有roads中所有小于maxDistance的路径
        # 先排除所有路径和大于maxDistance的路径
        res = 0
        opened = [0] * n
        for mask in range(1 << n):
            for i in range(n):
                opened[i] = mask & (1 << i)

            d = [[99999999] * n for int in range(n)]
            for i, j, r in roads:
                if opened[i] and opened[j]:
                    d[i][j] = d[j][i] = min(d[i][j], r)

            for k in range(n):
                if opened[k]:
                    for i in range(n):
                        if opened[i]:
                            for j in range(n):
                                if opened[j]:
                                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

            good = 1
            for i in range(n):
                if opened[i]:
                    for j in range(i + 1, n):
                        if opened[j]:
                            if d[i][j] > maxDistance:
                                good = 0
                                break
                if not good:
                    break
            res += good

        return res
