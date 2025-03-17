class FreqStack(object):

    def __init__(self):
        # 初始化列表
        self.stack = []
        self.map = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.map.get(val) is not None:
            self.map[val] = self.map[val] + 1
        else:
            self.map[val] = 1

    def pop(self):
        """
        :rtype: int
        """
        key = max(self.map, key=self.map.get)
        self.stack.remove(key)
        val = self.map[key]
        if val is not None:
            self.map[key] = val - 1
            if self.map[key] == 0:
                del self.map[key]

        print(key)
        print(self.map)
        print(self.stack)
        return key



# Your FreqStack object will be instantiated and called as such:
freqStack = FreqStack()
freqStack.push(5)    #堆栈为 [5]
freqStack.push(7)    #堆栈是 [5,7]
freqStack.push(5)    #堆栈是 [5,7,5]
freqStack.push(7)    #堆栈是 [5,7,5,7]
freqStack.push(4)    #堆栈是 [5,7,5,7,4]
freqStack.push(5)    #堆栈是 [5,7,5,7,4,5]
print('ret', freqStack.pop())      #返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
print('ret', freqStack.pop())      #返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
print('ret', freqStack.pop())      #返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
print('ret', freqStack.pop())      #返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
