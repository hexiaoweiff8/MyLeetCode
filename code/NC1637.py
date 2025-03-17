class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xArray = []
        for point in points:
            xArray.append(point[0])

        xArray.sort()
        maxScope = 0
        for index in range(1, len(xArray)):
            scope = xArray[index] - xArray[index - 1]
            if scope > maxScope:
                maxScope = scope

        return maxScope


obj = Solution()
print(obj.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
