class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(h)
        horizontalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.append(0)
        horizontalCuts.sort()
        verticalCuts.sort()
        maxVerGap = maxHorGap = 0
        for i in range(1, len(horizontalCuts)):
            maxHorGap = max(maxHorGap, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            maxVerGap = max(maxVerGap, verticalCuts[i] - verticalCuts[i - 1])
        if maxHorGap == 0:
            if len(horizontalCuts) == 1:
                maxHorGap = max(horizontalCuts[0], h - horizontalCuts[0])
            else:
                maxHorGap = h
        if maxVerGap == 0:
            if len(verticalCuts) == 1:
                maxVerGap = max(verticalCuts[0], w - verticalCuts[0])
            else:
                maxVerGap = w
        return maxHorGap * maxVerGap % (10 ** 9 + 7)


obj = Solution()
# print(obj.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
# print(obj.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
print(obj.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
# print(obj.maxArea(h=2, w=7, horizontalCuts=[1], verticalCuts=[2, 1, 5]))
print(obj.maxArea(h=5, w=2, horizontalCuts=[3, 1, 2], verticalCuts=[1]))

