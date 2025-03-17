import bisect
from collections import defaultdict


class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        return bisect.bisect_right(self.pos[value], right) - bisect.bisect_left(self.pos[value], left)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)