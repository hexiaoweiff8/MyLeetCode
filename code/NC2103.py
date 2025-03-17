class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        dic = {}
        ret = 0
        for index, char in enumerate(rings):
            print(dic, index, char)
            if index % 2 == 0:
                color = char
            else:
                i = int(char)
                tmpSet = dic.get(i, set())
                if len(tmpSet) != 3:
                    tmpSet.add(color)
                    dic[i] = tmpSet
                    if len(dic[i]) == 3:
                        ret += 1
        return ret


obj = Solution()
print(obj.countPoints("B0B6G0R6R0R6G9"))
# print(obj.countPoints("B0R0G0R9R0B0G0"))
