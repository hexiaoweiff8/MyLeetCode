class StockSpanner(object):

    def __init__(self):
        self.stack = [(-1, float("inf"))]
        self.index = -1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.index += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.index, price))
        return self.index - self.stack[-2][0]




# Your StockSpanner object will be instantiated and called as such:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85))