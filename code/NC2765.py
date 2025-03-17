import math


class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = maxRet = ret = 0
        preNum = nums[0]
        while index < len(nums):
            if preNum + math.pow(-1, ret) == nums[index]:
                ret += 1
                maxRet = max(maxRet, ret)
            else:
                if ret > 0:
                    index -= 1
                ret = 0
            preNum = nums[index]
            index += 1
        return (maxRet + 1) if 0 < maxRet else -1


obj = Solution()
# print(obj.alternatingSubarray([2, 3, 4, 3, 4]))
print(obj.alternatingSubarray([21, 9, 5]))
