class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mod = 10 ** 9 + 7
        ret = s = 0
        for num in nums:
            ret = (ret + num * num * (num + s)) % mod
            s = (s * 2 + num) % mod

        return ret


obj = Solution()
print(obj.sumOfPower(nums=[2, 1, 4]))
