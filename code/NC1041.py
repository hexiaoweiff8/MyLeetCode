class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x = 0
        y = 0
        dir = 0
        for _ in range(4):
            for cmd in instructions:
                if cmd == "L":
                    dir -= 1
                elif cmd == "R":
                    dir += 1
                else:
                    if dir == 0:
                        # 上
                        y += 1
                    elif dir == 1:
                        # 右
                        x += 1
                    elif dir == 2:
                        # 下
                        y -= 1
                    else:
                        # 左
                        x -= 1
                    pass
                if dir >= 4:
                    dir = 0
                elif dir < 0:
                    dir = 3

            if x == 0 and y == 0:
                return True

        return False




obj = Solution()
print(obj.isRobotBounded("GGLLGG"))
print(obj.isRobotBounded("GG"))
print(obj.isRobotBounded("GL"))
print(obj.isRobotBounded("GLGLGGLGL"))
