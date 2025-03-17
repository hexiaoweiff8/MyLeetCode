class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - ret > 0:
                batteryPercentages[i] = max(0, batteryPercentages[i] - ret)
                ret += 1
        return ret


obj = Solution()
print(obj.countTestedDevices([1,1,2,1,3]))