class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        group1, group2 = {}, {}
        for i, costList in enumerate(cost):
            group1[i] = min(costList)
            for j, costVal in enumerate(costList):
                group2[j] = min(group2.get(j, 0), costVal)
