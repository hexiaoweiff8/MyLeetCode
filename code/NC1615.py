class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if not roads or not n:
            return 0
        # 预处理
        roadDic = {}
        ret = 0
        for road in roads:
            road1 = road[0]
            road2 = road[1]
            dirList1 = roadDic.get(road1, [])
            dirList2 = roadDic.get(road2, [])
            dirList1.append(road2)
            dirList2.append(road1)
            roadDic[road1] = dirList1
            roadDic[road2] = dirList2

        # 记忆字典计算城市间值
        for index in range(n):
            roadList1 = roadDic.get(index, [])
            roadListLen1 = len(roadList1)
            for index2 in range(index + 1, n):
                roadList2 = roadDic.get(index2, [])
                # 去重求总和是否超过最大
                sumVal = roadListLen1 + len(roadList2) - (1 if index2 in roadList1 else 0)
                if sumVal > ret:
                    ret = sumVal

        return ret


obj = Solution()
print(obj.maximalNetworkRank(6, [[2, 4]]))
