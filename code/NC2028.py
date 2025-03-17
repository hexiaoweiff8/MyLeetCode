class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        rollsTotal = sum(rolls)
        allTotal = (m + n) * mean
        diff = allTotal - rollsTotal
        nMean = diff / float(n)
        ret = []
        if nMean > 6 or nMean < 1:
            return []
        nMean = int(nMean)
        for i in range(n - 1):
            ret.append(nMean)
            diff -= nMean
        index = len(ret) - 1
        while diff > 6:
            diff -= 6 - ret[index]
            ret[index] += 6 - ret[index]
            index -= 1
        ret.append(diff)
        return ret


obj = Solution()
# print(obj.missingRolls([3, 2, 4, 3], 4, 2))
# print(obj.missingRolls([1, 5, 6], 3, 4))
# print(obj.missingRolls([1, 2, 3, 4], 6, 4))
# print(obj.missingRolls([3, 5, 3], 5, 3))
print(obj.missingRolls([4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5], 4,
                       40))
