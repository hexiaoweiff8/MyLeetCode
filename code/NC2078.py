class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        maxRange = 0
        for i in range(n):
            for j in range(n - 1, i, -1):
                if colors[i] != colors[j]:
                    maxRange = max(maxRange, j - i)

        return maxRange

