class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.memory = [0] * n

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        free = 0
        for i in range(self.n):
            if self.memory[i] == 0:
                free += 1
                if free == size:
                    self.memory[i - size + 1:i + 1] = [mID] * size
                    return i - size + 1
            else:
                free = 0
        return -1

    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        ret = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                ret += 1
        return ret

# Your Allocator object will be instantiated and called as such:
obj = Allocator(10)
print(obj.allocate(1, 1))
print(obj.allocate(1, 2))
print(obj.allocate(1, 3))
print(obj.freeMemory(2))
print(obj.allocate(3, 4))
print(obj.allocate(1, 1))
print(obj.allocate(1, 1))
print(obj.freeMemory(1))
print(obj.allocate(10, 2))
print(obj.freeMemory(7))
