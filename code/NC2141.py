class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        l, r = 0, sum(batteries) // n + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if sum(min(b, mid) for b in batteries) >= n * mid:
                l = mid
            else:
                r = mid

        return l
