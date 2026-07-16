class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]
        n = len(nums)
        prefixGcd = []

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd.append(gcd(mx, nums[i]))

        prefixGcd.sort()
        ans = 0
        for i in range(n // 2):
            ans += gcd(prefixGcd[i], prefixGcd[n - i - 1])
        return ans