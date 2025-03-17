from sortedcontainers import SortedList

class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.m = m
        self.k = k
        self.doubleK = k + k
        self.allVal = []
        self.avgVal = SortedList()
        self.maxVal = []
        self.minVal = []
        self.count = 0
        self.minCount = 0
        self.maxCount = 0
        self.avgSum = 0

    # 添加元素
    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.count < self.doubleK:
            self.avgVal.add(num)
            if self.count + 1 == self.doubleK:
                # 分配avgVal的内容到maxVal和minVal
                self.minVal = SortedList(self.avgVal[:(self.count + 1) // 2])
                self.maxVal = SortedList(self.avgVal[(self.count + 1) // 2:])
                self.avgVal.clear()
        else:
            # 对比是否进去前k列表, 对比是否进入后k列表
            if self.maxVal[0] < num:
                self.maxVal.add(num)
            elif self.minVal[-1] > num:
                self.minVal.add(num)
            else:
                self.avgVal.add(num)
                self.avgSum += num

            # 删除元素
            if self.count + 1 > self.m:
                popVal = self.allVal.pop(0)
                if popVal in self.avgVal:
                    self.avgVal.remove(popVal)
                    self.avgSum -= popVal
                elif popVal in self.minVal:
                    self.minVal.remove(popVal)
                    maxMinVal = self.avgVal.pop(0)
                    self.minVal.add(maxMinVal)
                    self.avgSum -= maxMinVal
                elif popVal in self.maxVal:
                    self.maxVal.remove(popVal)
                    minMaxVal = self.avgVal.pop()
                    self.maxVal.add(minMaxVal)
                    self.avgSum -= minMaxVal
                self.count -= 1

        if len(self.maxVal) > self.k:
            popVal = self.maxVal.pop(0)
            self.avgSum += popVal
            self.avgVal.add(popVal)
        if len(self.minVal) > self.k:
            popVal = self.minVal.pop()
            self.avgSum += popVal
            self.avgVal.add(popVal)

        self.allVal.append(num)
        self.count += 1
        print(self.allVal)
        print(self.minVal, self.avgVal, self.maxVal)

    # 计算mk均值
    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if self.count < self.m:
            return -1
        return int(self.avgSum / (self.count - self.doubleK))


# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
# for i in range(10000):
#     obj.addElement(random.randint(1, 1000))
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
print(obj.calculateMKAverage())
