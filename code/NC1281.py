class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        numArray = []
        aSum, bSum = 1, 0
        while n:
            numArray.append(n % 10)
            n //= 10
        for num in numArray:
            aSum *= num
            bSum += num
        return aSum - bSum


obj = Solution()
print(obj.subtractProductAndSum(234))
print(obj.subtractProductAndSum(4421))