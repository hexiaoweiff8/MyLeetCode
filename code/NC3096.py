class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        n = len(possible)
        preList = [0] * n
        preList[0] = 1 if possible[0] == 1 else -1
        for i in range(1, n):
            preList[i] = preList[i - 1] + (1 if possible[i] == 1 else -1)
        ret = 0
        for i in range(n - 1):
            ret += 1
            if preList[i] - (preList[n - 1] - preList[i]) > 0:
                return ret

        return -1


obj = Solution()
print(obj.minimumLevels([1, 1]))
