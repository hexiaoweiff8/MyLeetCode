from itertools import count


class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        ret1 = ret2 = 0
        red2 = red1 = red
        blue2 = blue1 = blue
        for i in count(1):
            if i % 2:
                red1 -= i
                blue2 -= i
            else:
                red2 -= i
                blue1 -= i
            if red1 >= 0 and blue1 >= 0:
                ret1 += 1
            if red2 >= 0 and blue2 >= 0:
                ret2 += 1
            if (red1 < 0 or blue1 < 0) and (red2 < 0 or blue2 < 0):
                return max(ret1, ret2)