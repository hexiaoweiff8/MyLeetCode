class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = nums[0]
        index = 0
        isUp = nums[0] < nums[1]
        sumArray = [0, 0, 0]
        for i in range(1, len(nums)):
            if isUp:
                if nums[i] <= pre:
                    index += 1
                    isUp = False
            else:
                if nums[i] >= pre:
                    index += 1
                    isUp = True
            pre = nums[i]
            sumArray[index] += nums[i]
            if index > 2:
                break

        return max(sumArray)


obj = Solution()
print(obj.maxSumTrionic([0, -2, -1, -3, 0, 2, -1]))
