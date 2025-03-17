class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        preX = points[0][0]
        ret = 1
        for i in range(len(points)):
            if points[i][0] - preX > w:
                ret += 1
                preX = points[i][0]

        return ret

