class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        ret = 0
        gbArray = [[0, 0, 0]]
        for i in range(len(garbage) - 1, -1, -1):
            oneGarbage = garbage[i]
            gbArray.insert(0, [oneGarbage.count("M") + gbArray[0][0],
                            oneGarbage.count("P") + gbArray[0][1],
                            oneGarbage.count("G") + gbArray[0][2]])
        ret += sum(gbArray[0])
        for i in range(1, len(gbArray) - 1):
            if gbArray[i][0] != 0:
                ret += travel[i - 1]
            if gbArray[i][1] != 0:
                ret += travel[i - 1]
            if gbArray[i][2] != 0:
                ret += travel[i - 1]
        return ret


obj = Solution()
print(obj.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
