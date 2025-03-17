class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        @cache
        # 下表从1开始
        def dfs(i):
           if i << 1 >= len(prices):
               return prices[i - 1]
           return min(dfs(j) for j in range(i + 1, i * 2 + 2)) + prices[i - 1]
        return dfs(1)


obj = Solution()
print(obj.minimumCoins([3, 1, 2]))
