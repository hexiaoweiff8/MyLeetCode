class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        return max(special[0] - bottom,
                   top - special[-1],
                   *(special[i] - special[i - 1] - 1 for i in range(1, len(special)))
                   )