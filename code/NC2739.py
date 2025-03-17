class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        ret = 0
        while mainTank >= 5:
            mainTank -= 5
            ret += 50
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1
        if mainTank > 0:
            ret += mainTank * 10
        return ret


obj = Solution()
print(obj.distanceTraveled(9, 2))