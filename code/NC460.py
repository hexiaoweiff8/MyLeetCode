from collections import defaultdict


class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'

    def __init__(self, key=0, val=0):
        self.key = key
        self.value = val
        self.freq = 1  #  新书只读了一次

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = dict()
        def new_list():
            dummy = Node()  # 哨兵节点
            dummy.prev = dummy
            dummy.next = dummy
            return dummy
        self.freq_to_dummy = defaultdict(new_list)

    def get_node(self, key):
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:  # 抽出来后，这摞书是空的
            del self.freq_to_dummy[node.freq]  # 移除空链表
            if self.min_freq == node.freq:  # 这摞书是最左边的
                self.min_freq += 1
        node.freq += 1  # 看书次数 +1
        self.push_front(self.freq_to_dummy[node.freq], node)  # 放在右边这摞书的最上面
        return node

    def get(self, key):
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key, value):
        node = self.get_node(key)
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        if len(self.key_to_node) == self.capacity:  # 书太多了
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev  # 最左边那摞书的最下面的书
            print("dekey:", back_node.key)
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 移除
            if dummy.prev == dummy:  # 这摞书是空的
                del self.freq_to_dummy[self.min_freq]  # 移除空链表
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(self.freq_to_dummy[1], node)  # 放在「看过 1 次」的最上面
        self.min_freq = 1

    # 删除一个节点（抽出一本书）
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放在最上面）
    def push_front(self, dummy, x):
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# print(obj.get(3))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
# print("--------------------------------")

# obj = LFUCache(2)
# obj.put(3, 1)
# obj.put(2, 1)
# obj.put(2, 2)
# obj.put(4, 4)
# print(obj.get(2))
# print("--------------------------------")

# obj = LFUCache(2)
# obj.put(2, 1)
# obj.put(3, 2)
# print(obj.get(3))
# print(obj.get(2))
# obj.put(4, 3)
# print(obj.get(2))
# print(obj.get(3))
# print(obj.get(4))
# 2 1 1 -1 3
# print("--------------------------------")

# obj = LFUCache(3)
# obj.put(2, 2)
# obj.put(1, 1)
# print(obj.get(2))
# print(obj.get(1))
# print(obj.get(2))
# obj.put(3, 3)
# obj.put(4, 4)
# print(obj.get(3))
# print(obj.get(2))
# print(obj.get(1))
# print(obj.get(4))
# # 2 1 1 -1 3
# print("--------------------------------")

op = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
      "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
      "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
      "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
      "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
      "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
      "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
val = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
       [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
       [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
       [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26],
       [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28],
       [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12],
       [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1],
       [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

rightVal = [-1, 19, 17, -1, -1, -1, 5, -1, 12, 3, 5, 5, 1, -1, 30, 5, 30, -1, -1, 24, 18, 14, 18, 11, 18, -1, 4, 29, 30,
            12, 11, 29, 17, -1, 18, -1, 20, 29, 18, 18, 20]
index2 = 0
for index, item in enumerate(op):
    if item == "LFUCache":
        obj = LFUCache(val[index][0])
    elif item == "put":
        obj.put(val[index][0], val[index][1])
        print("put:", val[index][0], val[index][1])
    else:
        valRet = obj.get(val[index][0])
        print("get: ", val[index][0], valRet, rightVal[index2], valRet == rightVal[index2])
        index2 += 1
