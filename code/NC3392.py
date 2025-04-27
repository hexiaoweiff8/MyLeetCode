
class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((nums[i - 1] + nums[i + 1]) * 2 == nums[i] for i in range(1, len(nums) - 1))


obj = Solution()
# print(obj.countSubarrays([1,2,1,4,1]))
print(obj.countSubarrays([-2, 4, -2]))
