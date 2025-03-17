class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        startI = 1
        i = 1
        count = 1
        i = self.doCycle(i, n)
        while i != startI:
            i = self.doCycle(i, n)
            count += 1
        return count

    # 执行判断
    def doCycle(self, i, n):
        if i % 2 == 0:
            i = i / 2
        else:
            i = n / 2 + (i - 1) / 2
        return i

obj = Solution()
print(obj.reinitializePermutation(1200))
