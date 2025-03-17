class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        index = 0
        for bus in buses:
            c = capacity
            while c and index < len(passengers) and passengers[index] <= bus:
                c -= 1
                index += 1

        index -= 1
        ret = buses[-1] if c else passengers[index]
        while index >= 0 and passengers[index] == ret:
            index -= 1
            ret -= 1
        return ret



obj = Solution()
# print(obj.latestTimeCatchTheBus(buses=[10,20], passengers=[2,17,18,19], capacity=2))
# print(obj.latestTimeCatchTheBus(buses=[20,30,10], passengers=[19,13,26,4,25,11,21], capacity=2))
print(obj.latestTimeCatchTheBus(buses=[3], passengers=[2, 4], capacity=2))
