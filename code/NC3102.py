from sortedcontainers import SortedList


class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xs = SortedList()
        ys = SortedList()
        for x, y in points:
            xs.add(x + y)
            ys.add(y - x)

        ret = 99999999999
        for x, y in points:
            xs.remove(x + y)
            ys.remove(y - x)
            ret = min(ret, max(xs[-1] - xs[0], ys[-1] - ys[0]))
            xs.add(x + y)
            ys.add(y - x)

        return ret