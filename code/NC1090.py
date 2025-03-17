class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        ret = 0
        labelDic = {}
        unionList = list(zip(values, labels))
        unionList.sort(key=lambda item: item[0], reverse=True)
        for val, lab in unionList:
            if labelDic.get(lab, 0) < useLimit:
                labelDic[lab] = labelDic.get(lab, 0) + 1
                ret += val
                if numWanted == sum(labelDic.values()):
                    break

        return ret


obj = Solution()
print(obj.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], numWanted=3, useLimit=1))
print(obj.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], numWanted=3, useLimit=2))
print(obj.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], numWanted=3, useLimit=1))
