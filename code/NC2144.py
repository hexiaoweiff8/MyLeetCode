class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        ans = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                ans += cost[n - i - 1]
        return ans