class Solution(object):
    def maxArrayValue(self, nums):
        if not nums:
            return 0
        val = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            val = val + nums[index] if nums[index] <= val else nums[index]
        return val


obj = Solution()
# print(obj.maxArrayValue([2, 3, 7, 9, 3]))
# print(obj.maxArrayValue([5, 3, 3]))
print(obj.maxArrayValue([40, 15, 35, 98, 77, 79, 24, 62, 53, 84, 97, 16, 30, 22, 49]))
