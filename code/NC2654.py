class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num1 = 0
        res = 0
        # 最大公约数方法
        # 最大公约数方法
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        for x in nums:
            if x == 1:
                num1 += 1
            res = gcd(res, x)

        if num1 > 0:
            return n - num1
        if res > 1:
            return -1

        minLen = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    minLen = min(minLen, j - i + 1)
                    break

        return minLen + n - 2
