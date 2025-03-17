class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        ret = 0
        for i in range(total // cost1 + 1):
            ret += (total - i * cost1) // cost2 + 1
        return ret


obj = Solution()
print(obj.waysToBuyPensPencils(total=20, cost1=10, cost2=5))
