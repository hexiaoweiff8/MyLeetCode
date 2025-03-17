class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for start, end in self.calendar:
            if (startTime <= start < endTime)\
                    or (startTime < end <= endTime)\
                    or (startTime <= start and endTime >= end)\
                    or (startTime >= start and endTime <= end):
                return False
        self.calendar.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(23, 32))
print(obj.book(42, 50))
print(obj.book(6, 14))
print(obj.book(0, 7))
print(obj.book(21, 30))
print(obj.book(26, 31))
