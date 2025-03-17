class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        # 枚举方法
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            pre = psum = maxHeights[i]
            for j in range(i - 1, -1, -1):
                pre = min(pre, maxHeights[j])
                psum += pre
            suf = maxHeights[i]
            for j in range(i + 1, n):
                suf = min(suf, maxHeights[j])
                psum += suf
            ans = max(ans, psum)
        return ans
