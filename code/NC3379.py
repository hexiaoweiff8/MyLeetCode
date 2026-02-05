class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]


obj = Solution()
print(obj.constructTransformedArray([-1,4,-1]))