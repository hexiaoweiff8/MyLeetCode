class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ret = 0
        for coin in coins:
            ret += coin // 2 + (1 if coin % 2 == 1 else 0)
        return ret