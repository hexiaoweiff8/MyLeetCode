class MyHashMap(object):

    def __init__(self):
        self.hashMod = 1000001
        self.array = [-1 for _ in range(self.hashMod)]

    def put(self, key, value):
        # 将key进行hash获取int的hash值
        self.array[hash(key) % self.hashMod] = value

    def get(self, key):
        return self.array[hash(key) % self.hashMod]

    def remove(self, key):
        self.array[hash(key) % self.hashMod] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1,value)
# param_2 = obj.get(key)
# obj.remove(key)