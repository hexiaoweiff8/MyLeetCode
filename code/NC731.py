class MyCalendarTwo(object):

    def __init__(self):
        self.scope1 = []
        self.scope2 = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for start, end in self.scope2:
            if self.check(startTime, endTime, start, end):
                return False
        for start, end in self.scope1:
            startScope, endScope = self.getScope(startTime, endTime, start, end)
            if startScope is not None and endScope is not None:
                self.scope2.append((startScope, endScope))
        self.scope1.append((startTime, endTime))
        return True

    def check(self, startTime, endTime, start, end):
        return (startTime <= start < endTime) \
            or (startTime < end <= endTime) \
            or (startTime <= start and endTime >= end) \
            or (startTime >= start and endTime <= end)

    def getScope(self, startTime, endTime, start, end):
        # 获取区间的交集
        if startTime <= start < endTime:
            return start, min(endTime, end)
        if startTime < end <= endTime:
            return max(startTime, start), end
        if startTime <= start and endTime >= end:
            return start, end
        if startTime >= start and endTime <= end:
            return startTime, endTime
        return None, None

# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
# print(obj.book(10, 20))
# print(obj.book(50, 60))
# print(obj.book(10, 40))
# print(obj.book(5, 15))
# print(obj.book(5, 10))
# print(obj.book(25, 55))

print(obj.book(5, 12))
print(obj.book(42, 50))
print(obj.book(4, 9))
print(obj.book(33, 41))
print(obj.book(2, 7))
print(obj.book(16, 25))
print(obj.book(7, 16))
print(obj.book(6, 11))
print(obj.book(13, 18))
print(obj.book(38, 43))
print(obj.book(49, 50))
print(obj.book(6, 15))
print(obj.book(5, 13))
print(obj.book(35, 42))
print(obj.book(19, 24))
print(obj.book(46, 50))
print(obj.book(39, 44))
print(obj.book(28, 36))