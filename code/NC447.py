class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            d = {}
            for q in points:
                dis = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                d[dis] = d.get(dis, 0) + 1
            for v in d.values():
                res += v * (v - 1)
        return res
