class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dirDic = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        s = {(x, y) for x, y in obstacles}
        ret, x, y, d = 0, 0, 0, 0
        for command in commands:
            if command == -2:
                d = (d + 3) % 4
            elif command == -1:
                d = (d + 1) % 4
            else:
                for _ in range(command):
                    xP, yP = x + dirDic[d][0], y + dirDic[d][1]
                    if (xP, yP) in s:
                        break
                    x, y = xP, yP
                    ret = max(ret, x * x + y * y)

        return ret


obj = Solution()
print(obj.robotSim(commands=[4, -1, 3], obstacles=[]))
print(obj.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))
print(obj.robotSim([6, -1, -1, 6], []))
print(obj.robotSim([-2, -1, 8, 9, 6],
                   [[-1, 3], [0, 1], [-1, 5], [-2, -4], [5, 4], [-2, -3], [5, -1], [1, -1], [5, 5], [5, 2]]))
print(obj.robotSim([7, -2, -2, 7, 5],
                   [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]))
