class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        ret = []
        for index in range(1, len(mountain) - 1):
            if mountain[index - 1] < mountain[index] > mountain[index + 1]:
                ret.append(index)
        return ret
