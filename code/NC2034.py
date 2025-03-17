from sortedcontainers import SortedList


class StockPrice(object):

    def __init__(self):
        self.dic = {}
        self.prices = SortedList()
        self.max_current_price_timestamp = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.dic:
            self.prices.discard(self.dic[timestamp])
        self.dic[timestamp] = price
        self.prices.add(price)
        self.max_current_price_timestamp = max(self.max_current_price_timestamp, timestamp)

    def current(self):
        """
        :rtype: int
        """
        return self.dic[self.max_current_price_timestamp]

    def maximum(self):
        """
        :rtype: int
        """
        return self.prices[-1]

    def minimum(self):
        """
        :rtype: int
        """
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
stockPrice = StockPrice()
stockPrice.update(1, 10)
stockPrice.update(2, 5)
print(stockPrice.current())
print(stockPrice.maximum())
stockPrice.update(1, 3)
print(stockPrice.maximum())
stockPrice.update(4, 2)
print(stockPrice.minimum())
