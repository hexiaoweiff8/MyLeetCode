class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                del self.cache[self.queue.pop(0)]
        else:
            self.queue.remove(key)
        self.cache[key] = value
        self.queue.append(key)




# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
print(obj.get(1))
print(obj.get(2))
