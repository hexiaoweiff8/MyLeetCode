class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # 左往右滑动匹配
        lenNums = len(nums)
        leftIndex = 0
        rightIndex = 0
        leftSum = 0
        rightSum = sum(nums)
        minCount = lenNums + 1
        if rightSum == x:
            return lenNums
        if rightSum < x:
            return -1
        for leftIndex in range(-1, lenNums - 1):
            if leftIndex > -1:
                leftSum += nums[leftIndex]
            while leftSum + rightSum > x and rightIndex < lenNums:
                rightSum -= nums[rightIndex]
                rightIndex += 1
            if leftSum + rightSum == x:
                minCount = min(minCount, leftIndex + 1 + lenNums - rightIndex)

        return -1 if minCount > lenNums else minCount


nums = [5, 1, 4, 2, 3]
x = 6
obj = Solution()
print(obj.minOperations(nums, x))
