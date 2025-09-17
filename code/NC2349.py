import heapq
from collections import defaultdict


class NumberContainers(object):

    def __init__(self):
        self.dic = defaultdict(list)
        self.hash = {}

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.hash[index] = number
        heapq.heappush(self.dic[number], index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        indices = self.dic[number]
        while indices and self.hash[indices[0]] != number:
            heapq.heappop(indices)
        return indices[0] if indices else -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)