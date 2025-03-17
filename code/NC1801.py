class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        dict = {}
        for item in orders:
            count = dict.get(item, 0) + 1
            if count >= 2:
                return item
            dict[item] = count

obj = Solution()
print(obj.getNumberOfBacklogOrders('abcdd'))
