class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # 计算以cur为前缀的数字数量
        def getCount(cur, n):
            count = 0
            first = cur
            last = cur
            while first <= n:
                count += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return count

        # 从1到9遍历，找到第k小的数字
        cur = 1
        k -= 1  # 因为索引从0开始
        while k > 0:
            count = getCount(cur, n)
            if k >= count:
                k -= count
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur