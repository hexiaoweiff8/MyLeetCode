class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius + 273.15, celsius * 1.8 + 32]


obj = Solution()
print(obj.convertTemperature(122.11))
