class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 找到所有平行于x周线的线段
        y_linex = {}
        for p1, p2 in points:
            if p2 in y_linex:
                y_linex[p2].append(p1)
            else:
                y_linex[p2] = [p1]

        count = sumV = 0
        for cnt in y_linex.values():
            k = len(cnt) * (len(cnt) - 1) // 2
            count += sumV * k
            sumV += k

        return count % (10 ** 9 + 7)


obj = Solution()
print(obj.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
