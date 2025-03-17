class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hisDic = {"row": [[] for _ in range(len(grid))], "col": [[] for _ in range(len(grid[0]))]}
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    hisDic["row"][row].append(col)
                    hisDic["col"][col].append(row)

        for row in hisDic["row"]:
            if len(row) > 1:
                ret += len(row)
        for colIndex, col in enumerate(hisDic["col"]):
            if len(col) > 1:
                ret += len(col)
                for row in col:
                    if len(hisDic["row"][row]) > 1 and colIndex in hisDic["row"][row]:
                        ret -= 1
        return ret


obj = Solution()
print(obj.countServers([[1,0],[0,1]]))
print(obj.countServers([[1,0],[1,1]]))
print(obj.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
