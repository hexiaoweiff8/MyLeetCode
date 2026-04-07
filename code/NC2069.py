class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.index = 0


    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.index = (self.index + num - 1) % ((self.width + self.height - 2) * 2) + 1

    def getPos(self):
        """
        :rtype: List[int]
        """
        # 计算落在四边哪个位置
        if self.index < self.width:
            self.dir = 'East'
            return [self.index, 0]
        elif self.index < self.width + self.height - 1:
            self.dir = 'North'
            return [self.width - 1, self.index - self.width + 1]
        elif self.index < self.width * 2 + self.height - 2:
            self.dir = 'West'
            return [self.width * 2 + self.height - self.index - 3, self.height - 1]
        else:
            self.dir = 'South'
            return [0, (self.width + self.height) * 2 - self.index - 4]

    def getDir(self):
        """
        :rtype: str
        """
        self.getPos()
        return self.dir



# Your Robot object will be instantiated and called as such:
obj = Robot(6, 3)
print(obj.step(2))
print(obj.step(2))
print(obj.getPos())
print(obj.getDir())
print(obj.step(2))
print(obj.step(1))
print(obj.step(4))
print(obj.getPos())
print(obj.getDir())