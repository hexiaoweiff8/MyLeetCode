class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 把方向
        border = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # 边界max
        n = len(grid) - 1
        # 起终为1
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1
        if n == 0:
            return 1 if grid[0][0] == 0 else -1
        # 待处理列表
        openStack = {(0, 0): {"g": 1, "h": n + n}}
        closeDic = {(0, 0): {"g": 1, "h": n + n}}

        # 查找非关闭列表的0index列表
        def getPassIndexList(x, y, g):
            ret = {}
            for dx, dy in border:
                px, py = x + dx, y + dy
                if n >= px >= 0 and n >= py >= 0 and grid[py][px] == 0:
                    if (px, py) not in closeDic:
                        ret[(px, py)] = {"g": g, "h": getH(px, py)}
                    elif g <= closeDic[(px, py)]["g"]:
                        closeDic[(px, py)]["g"] = g
                        ret[(px, py)] = {"g": g, "h": getH(px, py)}
            return ret

        # 计算H值
        def getH(x, y):
            return max(n - x, n - y)

        # 从左上角开始, 如果不在关闭列表内, 则进入
        indexX = indexY = 0
        step = 1
        while True:
            # print(indexX, indexY)
            indexDic = getPassIndexList(indexX, indexY, step)
            if indexDic.get((n, n), None):
                return indexDic.get((n, n))["g"] + 1
            if not indexDic:
                # 无路可走
                if not openStack:
                    return -1
                step -= 1
                # 从开放列表获取index
                indexX, indexY = min(openStack.items(), key=lambda item: item[1]["g"] + item[1]["h"])[0]
                ghVal = openStack.get((indexX, indexY), {"g": step, "h": getH(indexX, indexY)})
                del openStack[(indexX, indexY)]
            else:
                # 放入开放列表
                for key, val in indexDic.items():
                    existItem = openStack.get(key, None)
                    if existItem:
                        if val["g"] + val["h"] <= existItem["g"] + existItem["h"]:
                            openStack[key] = val
                    else:
                        openStack[key] = val
                indexX, indexY = min(openStack.items(), key=lambda item: item[1]["g"] + item[1]["h"])[0]
                ghVal = openStack.get((indexX, indexY), {"g": step, "h": getH(indexX, indexY)})
                del openStack[(indexX, indexY)]
            closeDic[(indexX, indexY)] = ghVal
            step = ghVal["g"] + 1
            # print(indexX, indexY, ghVal)
        # return - 1


obj = Solution()
# print(min({(10, 20): (30, 40), (30, 40): (10, 20)}.items(), key=lambda item: item[1])[0])
# print(max({(10, 20): {"g": 10, "h": 20}, (0, 1): {'g': 11, 'h': 20}}.items(), key=lambda item: item[1]["g"] + item[1]["h"])[0])
# print(min({(0, 0): {'g': 1, 'h': 8}, (1, 0): {'g': 2, 'h': 4}, (2, 1): {'g': 3, 'h': 3}, (0, 2): {'g': 6, 'h': 4},
#      (2, 0): {'g': 2, 'h': 4}, (1, 3): {'g': 5, 'h': 3}, (3, 1): {'g': 3, 'h': 3}, (1, 4): {'g': 4, 'h': 3},
#      (0, 4): {'g': 6, 'h': 4}, (0, 3): {'g': 5, 'h': 4}}.items(), key=lambda item: item[1]["g"] + item[1]["h"]))
print(obj.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(obj.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(obj.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(obj.shortestPathBinaryMatrix([
    [0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]]))
print(obj.shortestPathBinaryMatrix([[0, 1, 0, 0, 0, 0],
                                    [0, 1, 0, 1, 1, 0],
                                    [0, 1, 1, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0],
                                    [1, 1, 1, 1, 1, 0],
                                    [1, 1, 1, 1, 1, 0]]))
print(obj.shortestPathBinaryMatrix([[0, 1, 0, 0, 0, 0],
                                    [0, 1, 0, 1, 1, 0],
                                    [0, 1, 1, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0],
                                    [1, 1, 1, 1, 1, 0],
                                    [1, 1, 1, 1, 1, 0]]))
print(obj.shortestPathBinaryMatrix(
    [[0, 0, 0, 0, 1, 1, 1, 1, 0],
     [0, 1, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0, 0, 1, 1],
     [0, 0, 1, 1, 1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0]]))

print(obj.shortestPathBinaryMatrix([[0, 0, 1, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 1],
                                    [0, 0, 1, 0, 1, 0, 0],
                                    [0, 0, 0, 1, 1, 1, 0],
                                    [1, 0, 0, 1, 1, 0, 0],
                                    [1, 1, 1, 1, 1, 0, 1],
                                    [0, 0, 1, 0, 0, 0, 0]]))
