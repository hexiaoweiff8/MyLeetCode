class Solution(object):
    def temperatureTrend(self, temperatureA, temperatureB):
        """
        :type temperatureA: List[int]
        :type temperatureB: List[int]
        :rtype: int
        """
        maxVal = eqVal = 0
        for i in range(1, len(temperatureA)):
            if temperatureA[i] > temperatureA[i - 1] and temperatureB[i] > temperatureB[i - 1]:
                eqVal += 1
            elif temperatureA[i] < temperatureA[i - 1] and temperatureB[i] < temperatureB[i - 1]:
                eqVal += 1
            elif temperatureA[i] == temperatureA[i - 1] and temperatureB[i] == temperatureB[i - 1]:
                eqVal += 1
            else:
                maxVal = max(eqVal, maxVal)
                eqVal = 0

        maxVal = max(eqVal, maxVal)
        return maxVal



