class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        preX = points[0][0]
        preY = points[0][1]
        for i in range(1, len(points)):
            x = abs(preX - points[i][0])
            y = abs(preY - points[i][1])
            ans += abs(x - y) + min(x, y)
            preX = points[i][0]
            preY = points[i][1]
        return ans