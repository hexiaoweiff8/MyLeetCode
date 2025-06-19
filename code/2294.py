class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        minVal = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - minVal > k:
                ans += 1
                minVal = nums[i + 1]
        return ans


obj = Solution()
print(obj.partitionArray([3,6,1,2,5], 2))