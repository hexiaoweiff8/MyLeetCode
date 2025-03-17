class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        dic = {}
        reDic = {}
        existSet = set()
        for conn in connections:
            way = reDic.get(conn[0], [])
            way.append(conn[1])
            reDic[conn[0]] = way
            way = dic.get(conn[1], [])
            way.append(conn[0])
            dic[conn[1]] = way

        def dfs(nowCity):
            ret = 0
            nowCityList = []
            if nowCity in dic:
                nowCityList.extend(dic[nowCity])
                del dic[nowCity]
            if nowCity in reDic:
                for city in reDic[nowCity]:
                    if city not in existSet:
                        nowCityList.append(city)
                        ret += 1
                del reDic[nowCity]
            existSet.add(nowCity)
            for city in nowCityList:
                ret += dfs(city)
            return ret
        return dfs(0)

    def minReorder2(self, n, connections):
        e = [[] for _ in range(n)]
        for edge in connections:
            e[edge[0]].append([edge[1], 1])
            e[edge[1]].append([edge[0], 0])
        return self.dfs(0, -1, e)

    def dfs(self, x, parent, e):
        ret = 0
        for edge in e[x]:
            if edge[0] == parent:
                continue
            ret += edge[1] + self.dfs(edge[0], x, e)
        return ret



obj = Solution()
print(obj.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(obj.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
