class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        landNew = sorted(zip(landStartTime, landDuration))
        waterNew = sorted(zip(waterStartTime, waterDuration))

        landMin = min(landNew, key=lambda x: x[0] + x[1])
        waterMin = min(waterNew, key=lambda x: x[0] + x[1])
        landAns = landMin[0] + landMin[1]
        waterAns = waterMin[0] + waterMin[1]
        landMinVal = waterMinVal = 999999

        for i in range(len(landNew)):
            landMinVal = min(landMinVal, max(waterAns, landNew[i][0]) + landNew[i][1])
        for i in range(len(waterNew)):
            waterMinVal = min(waterMinVal, max(landAns, waterNew[i][0]) + waterNew[i][1])

        return min(landMinVal, waterMinVal)