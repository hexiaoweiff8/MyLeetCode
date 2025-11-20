class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 0
        s = e = -1
        for start, end in intervals:
            if start <= s:
                continue
            if start > e:
                res += 2
                s = end - 1
                e = end
            else:
                res += 1
                s = e
                e = end
        return res
