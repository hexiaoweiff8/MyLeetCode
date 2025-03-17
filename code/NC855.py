class ExamRoom(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.list = []

    def seat(self):
        """
        :rtype: int
        """
        # 靠左获取最远距离
        listLen = len(self.list)
        ret = 0
        if listLen == 0:
            self.list.append(0)
            ret = 0
        elif listLen == 1:
            # 判断左右最远距离
            val = self.list[0]
            dis1 = val - 0
            dis2 = self.n - 1 - val

            ret = 0 if dis1 > dis2 else (self.n - 1)
            self.list.append(ret)
        else:
            # 获取所有区间中靠左的最远区间中心位置
            preItem = -1
            maxDis = 0
            maxDisItem1 = -1
            maxDisItem2 = -1
            for item in self.list:
                if preItem >= 0:
                    gap = item - preItem
                    dis = gap // 2
                    if dis > maxDis:
                        maxDis = dis
                        maxDisItem1 = preItem
                        maxDisItem2 = item

                preItem = item

            # 判断0与n-1
            if 0 not in self.list:
                dis = self.list[0] - 0
                if dis >= maxDis:
                    maxDis = dis
                    maxDisItem1 = 0
                    maxDisItem2 = 0
            lastIndex = self.n - 1
            if lastIndex not in self.list:
                dis = lastIndex - self.list[listLen - 1]
                if dis > maxDis:
                    maxDisItem1 = lastIndex
                    maxDisItem2 = lastIndex
            if maxDisItem1 != -1 and maxDisItem2 != -1:
                ret = (maxDisItem1 + maxDisItem2) // 2
                self.list.append(ret)

        self.list.sort()
        print('ret', ret)
        return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        return self.list.remove(p)


# Your ExamRoom object will be instantiated and called as such:
opts = ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
        "leave", "leave", "seat", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave", "leave", "seat",
        "seat", "leave", "leave"]
vals = [[8], [], [], [], [0], [7], [], [], [], [], [], [], [], [0], [7], [], [], [7], [], [1], [], [3], [], [0], [5],
        [], [], [0], [6]]
obj = None
for index in range(len(opts)):
    print(index)
    opt = opts[index]
    val = vals[index]
    if opt == 'ExamRoom':
        obj = ExamRoom(val[0])
    elif opt == 'seat':
        obj.seat()
    elif opt == 'leave':
        obj.leave(val[0])

# obj = ExamRoom(10)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.leave(0))
# print(obj.leave(4))
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.leave(0))
