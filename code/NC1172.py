from sortedcontainers import SortedSet


class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = []
        self.notFullSet = SortedSet()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.notFullSet:
            self.stacks.append([val])
            if self.capacity > 1:
                self.notFullSet.add(len(self.stacks) - 1)
        else:
            index = self.notFullSet[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.notFullSet.discard(index)

    def pop(self):
        """
        :rtype: int
        """
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or len(self.stacks) <= index or len(self.stacks[index]) == 0:
            return -1
        val = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            while self.stacks and not self.stacks[-1]:
                self.notFullSet.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.notFullSet.add(index)
        return val


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
print(D.popAtStack(0))
D.push(20)
D.push(21)
print(D.popAtStack(0))
print(D.popAtStack(2))
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())