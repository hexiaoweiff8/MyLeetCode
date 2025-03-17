import heapq


class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.heap = [i for i in range(1, n+1)]


    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.heap)


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.heap, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)