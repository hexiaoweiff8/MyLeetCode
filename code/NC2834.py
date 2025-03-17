class Solution(object):
    # def minimumPossibleSum(self, n, target):
    #     nums = [0] * n
    #     val = 1
    #     for i in range(n):
    #         nums[i] = val
    #         if val < target:
    #             for j in range(0, i):
    #                 if nums[i] + nums[j] == target:
    #                     val = target
    #                     nums[i] = val
    #         val += 1
    #     return sum(nums) % 1000000007
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        m = target // 2
        if n <= m:
            return ((1 + n) * n // 2) % mod
        return ((1 + m) * m // 2 + (target * 2 + (n - m) - 1) * (n - m) // 2) % mod



obj = Solution()
print(obj.minimumPossibleSum(n=2, target=3))
print(obj.minimumPossibleSum(n=3, target=3))
print(obj.minimumPossibleSum(n=1, target=1))
