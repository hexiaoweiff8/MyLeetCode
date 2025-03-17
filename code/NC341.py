# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.list = []
        nestedList.reverse()
        self.stack = nestedList
        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.list.append(top.getInteger())
            else:
                tmpList = top.getList()
                tmpList.reverse()
                self.stack.extend(top.getList())

    def next(self):
        return self.list.pop(0)

    def hasNext(self):
        return len(self.list)

