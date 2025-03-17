class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.stream = [None] * n
        self.index = 0


    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value
        res = []
        while self.index < self.n and self.stream[self.index] is not None:
            res.append(self.stream[self.index])
            self.index += 1
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)