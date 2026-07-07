class Solution(object):
    def checkPowersOfThree(self, val):
        """
        :type n: int
        :rtype: bool
        """
        while val:
            if val % 3 == 2:
                return False
            val //= 3
        return True


obj = Solution()
print(obj.checkPowersOfThree(11))