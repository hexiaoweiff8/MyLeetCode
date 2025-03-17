from sortedcontainers import SortedSet
class SmallestInfiniteSet(object):

    def __init__(self):
        self.val = 1
        self.addValSet = SortedSet()

    def popSmallest(self):
        ret = self.val
        if self.addValSet and self.addValSet[0] <= self.val:
            if  self.addValSet[0] == self.val:
                self.val += 1
            ret = self.addValSet.pop(0)
        else:
            self.val += 1
        return ret

    def addBack(self, num):
        if num < self.val:
            self.addValSet.add(num)



smallestInfiniteSet = SmallestInfiniteSet()
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.addBack(1))
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.addBack(2))
print(smallestInfiniteSet.addBack(3))
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())