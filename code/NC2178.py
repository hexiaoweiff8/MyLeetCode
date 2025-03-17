class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        ret = []
        if finalSum % 2 == 1:
            return ret

        num = 2
        while num <= finalSum:
            ret.append(num)
            finalSum -= num
            num += 2
        ret[-1] += finalSum
        return ret


obj = Solution()
print(obj.maximumEvenSplit(12))
print(obj.maximumEvenSplit(28))
print(obj.maximumEvenSplit(10))