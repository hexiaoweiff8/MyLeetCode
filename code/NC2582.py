class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        mod = time % (2 * n - 1)
        return time + 1 if mod < n else n * 2 - mod - 1


obj = Solution()
print(obj.passThePillow(4, 5))
print(obj.passThePillow(4, 7))
print(obj.passThePillow(3, 2))
print(obj.passThePillow(18, 38))
