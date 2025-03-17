class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(price, k, mid):
                left = mid
            else:
                right = mid - 1
        return left

    # 多项区间二分查找
    def check(self, price, k, mid):
        priv = -999999999999
        cnt = 0
        for item in price:
            if item - priv >= mid:
                cnt += 1
                priv = item
        return cnt >= k


obj = Solution()
print(obj.maximumTastiness(price = [13,5,1,8,21,2], k = 3))
# print(obj.maximumTastiness(price = [1,3,1], k = 2))
# print(obj.maximumTastiness(price = [7,7,7,7], k = 2))
