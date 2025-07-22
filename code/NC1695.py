class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumVal = maxSum = 0
        leftIndex = 0
        hasVal = [False] * (max(nums) + 1)
        for i in range(len(nums)):
            sumVal += nums[i]
            if not hasVal[nums[i]]:
                hasVal[nums[i]] = True
            else:
                while hasVal[nums[i]]:
                    sumVal -= nums[leftIndex]
                    hasVal[nums[leftIndex]] = False
                    leftIndex += 1
                hasVal[nums[i]] = True

            maxSum = max(maxSum, sumVal)

        return maxSum