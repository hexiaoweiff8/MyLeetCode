class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 计算所有点之间的斜率并放入字典中
        slopes = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / float(p2[0] - p1[0])
                if slope in slopes:
                    slopes[slope].append((p1, p2))
                else:
                    slopes[slope] = [(p1, p2)]

        count = sumV = 0
        for cnt in slopes.values():
            k = len(cnt) * (len(cnt) - 1) // 2

        return count % (10 ** 9 + 7)


obj = Solution()
print(obj.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))
