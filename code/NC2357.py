class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        numsLen = len(nums)
        while max(nums) > 0:
            subVal = min(filter(lambda x: x > 0, nums))
            for index in range(numsLen):
                if nums[index] != 0:
                    nums[index] = nums[index] - subVal
            count += 1
        return count


obj = Solution()
print(obj.minimumOperations([1,5,0,3,5]))