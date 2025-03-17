class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        dic = {}
        for road in roads:
            roadList = dic.get(road[0], [])
            roadList.append(road[1])
            dic[road[0]] = roadList
            roadList = dic.get(road[1], [])
            roadList.append(road[0])
            dic[road[1]] = roadList
        self.ret = 0

        def dfs(cur, parentKey):
            nowSum = 1
            for key in dic.get(cur, []):
                if key != parentKey:
                    peopleCnt = dfs(key, cur)
                    nowSum += peopleCnt
                    self.ret += (peopleCnt + seats - 1) // seats
            return nowSum
        dfs(0, -1)
        return self.ret

