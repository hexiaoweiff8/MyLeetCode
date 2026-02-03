class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pre = nums[0]
        index = 0
        isUp = nums[0] < nums[1]
        if not isUp:
            return False
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return False
            if isUp:
                if nums[i] <= pre:
                    index += 1
                    isUp = False
            else:
                if nums[i] >= pre:
                    index += 1
                    isUp = True
            pre = nums[i]
            if index > 2:
                return False

        return index == 2


obj = Solution()
# print(obj.isTrionic([1,3,5,4,2,6]))
# print(obj.isTrionic([7,7,7]))
print(obj.isTrionic([2,4,3,3]))