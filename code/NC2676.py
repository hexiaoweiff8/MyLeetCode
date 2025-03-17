class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, n = 0, len(nums)
        for x in nums[(n + 1) // 2:]:
            if nums[i] * 2 <= x:
                i += 1
        return i * 2


object = Solution()
print(object.maxNumOfMarkedIndices([3,5,2,4]))