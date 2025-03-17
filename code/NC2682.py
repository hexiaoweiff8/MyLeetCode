class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        itemSet = set()
        index, step = 0, 1
        ret = []
        while index not in itemSet:
            itemSet.add(index)
            index = (index + step * k) % n
            step += 1
        for index in range(n):
            if index not in itemSet:
                ret.append(index + 1)
        return ret


obj = Solution()
print(obj.circularGameLosers(5, 2))
print(obj.circularGameLosers(4, 4))
print(obj.circularGameLosers(2, 1))
