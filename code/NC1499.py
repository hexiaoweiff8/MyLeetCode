class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        ret = -999999999999
        queue = []
        for x, y in points:
            while queue and queue[0][1] < x - k:
                queue.pop(0)
            if queue:
                ret = max(ret, x + y + queue[0][0])
            while queue and y - x >= queue[-1][0]:
                queue.pop()
            queue.append([y - x, x])
        return ret


obj = Solution()
print(obj.findMaxValueOfEquation(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1))
print(obj.findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3))
print(obj.findMaxValueOfEquation([[-19, 9], [-15, -19], [-5, -8]], 10))
