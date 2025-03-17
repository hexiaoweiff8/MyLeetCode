class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        stonesLen = len(stones)
        if stones[-1] - stones[0] + 1 == stonesLen:
            return [0, 0]
        maxCount = max(stones[-2] - stones[0] + 1, stones[-1] - stones[1] + 1) - (stonesLen - 1)
        minCount = stonesLen
        j = 0
        for i in range(stonesLen):
            while j + 1 < stonesLen and stones[j + 1] - stones[i] + 1 <= stonesLen:
                j += 1
            if j - i + 1 == stonesLen - 1 and stones[j] - stones[i] + 1 == stonesLen - 1:
                minCount = min(minCount, 2)
            else:
                minCount = min(minCount, stonesLen - (j - i + 1))

        return [minCount, maxCount]



