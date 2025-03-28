class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 0
        count = 0
        n2 = 1
        pre = 0
        hasJump = False
        while count < n:
            if pre + n2 >= k and not hasJump:
                n2 = k
                hasJump = True
            print(n2)
            ans += n2
            pre = n2
            n2 += 1
            count += 1
        return ans

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2


obj = Solution()
print(obj.minimumSum(n=5, k=4))
