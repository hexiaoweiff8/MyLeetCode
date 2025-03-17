class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        n = len(beans)
        beans.sort()
        total = sum(beans)
        ans = total
        for i in range(n):
            ans = min(ans, total - (n - i) * beans[i])
        return ans
