class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if k < numOnes:
            return k
        if k < numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)


obj = Solution()
print(obj.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2))
print(obj.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4))