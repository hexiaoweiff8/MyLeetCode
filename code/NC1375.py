class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        ret = mx = 0
        for index, flip in enumerate(flips, 1):
            mx = max(mx, flip)
            if mx == index:
                ret += 1
        return ret
