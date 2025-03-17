class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ret = 1 if nums[0] > 0 else 0
        index = 0
        while index < n - 2:
            if nums[index] < index + 1 < nums[index + 1]:
                ret += 1
            index += 1
        if n > nums[-1]:
            ret += 1
        return ret


obj = Solution()
print(obj.countWays([1, 1]))
print(obj.countWays([6, 0, 3, 3, 6, 7, 2, 7]))
# 0 2 3 3 6 6 7 7