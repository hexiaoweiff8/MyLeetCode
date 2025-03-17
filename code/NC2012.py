class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minLastArray = []
        maxPreVal = nums[0]
        minLastVal = nums[-1]
        ans = 0
        for i in range(n - 1, -1, -1):
            minLastVal = min(minLastVal, nums[i])
            minLastArray.insert(0, minLastVal)
        for i in range(1, n - 1):
            if maxPreVal < nums[i] < minLastArray[i + 1]:
                ans += 2
            elif nums[i + 1] > nums[i] > nums[i - 1]:
                ans += 1
            maxPreVal = max(maxPreVal, nums[i])
        return ans


obj = Solution()
print(obj.sumOfBeauties([1, 2, 3]))
print(obj.sumOfBeauties([2, 4, 6, 4]))
