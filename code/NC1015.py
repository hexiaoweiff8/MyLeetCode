class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        endNum = k % 10
        if endNum not in (1, 3, 7, 9):
            return -1

        ret, resid = 1, 1
        while resid % k != 0:
            resid = (resid % k) * (10 % k) + 1
            ret += 1

        return ret


obj = Solution()
print(obj.smallestRepunitDivByK(1))
print(obj.smallestRepunitDivByK(2))
print(obj.smallestRepunitDivByK(3))