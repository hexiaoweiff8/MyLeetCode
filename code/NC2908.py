class Solution(object):
    def minimumSum(self, nums):
        n = len(nums)
        res = mn = 1000
        left = [0] * n
        for i in range(1, n):
            left[i] = mn = min(nums[i - 1], mn)
        right = nums[n - 1]
        for i in range(n - 2, 0, -1):
            if left[i] < nums[i] and nums[i] > right:
                res = min(res, left[i] + nums[i] + right)
            right = min(right, nums[i])
        return res if res < 1000 else -1


obj = Solution()
print(obj.minimumSum([8, 6, 1, 5, 3]))
