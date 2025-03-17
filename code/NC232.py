class MyQueue(object):

    def __init__(self):
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.lst.pop(0) if self.lst else None


    def peek(self):
        """
        :rtype: int
        """
        return self.lst[0] if self.lst else None


    def empty(self):
        """
        :rtype: bool
        """

        return len(self.lst) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()