class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        # 构建map
        redDict = {}
        blueDict = {}
        ret = [0]
        ret2 = [0]
        isDouble = True
        for item in redEdges:
            list = redDict.get(item[1], [])
            list.append(item[0])
            redDict[item[1]] = item[0]
        for item in blueEdges:
            list = blueDict.get(item[1], [])
            list.append(item[0])
            blueDict[item[1]] = item[0]

        # 循环查找
        for index in range(n):
            if isDouble:
                first = redDict.get(index, None)
                second = blueDict.get(index, None)
            else:
                first = blueDict.get(index, None)
                second = redDict.get(index, None)
            isDouble = not isDouble
            print(first, second)
            ret.append(first if first is not None else -1)
            ret2.append(second if second is not None else -1)

        return ret, ret2


obj = Solution()
print(obj.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []))
# print(obj.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))
