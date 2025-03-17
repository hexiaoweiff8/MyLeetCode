from copy import copy


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 映射查找法
        # lenNums = len(nums)
        # numsIndexList = []
        # for index in range(lenNums):
        #     numsIndexList.append([nums[index], index])
        #
        # numsIndexList.sort()
        # left = 0
        # right = lenNums - 1
        # target1 = numsIndexList[left]
        # target2 = numsIndexList[right]
        # val = target1[0] + target2[0]
        # while left != right and val != target:
        #     if val > target:
        #         right -= 1
        #     elif val < target:
        #         left += 1
        #     else:
        #         break
        #     target1 = numsIndexList[left]
        #     target2 = numsIndexList[right]
        #     val = target1[0] + target2[0]
        # ret = [target1[1], target2[1]]
        # ret.sort()
        # return ret
        # 配对查找法
        for index in range(len(nums)):
            num = nums[index]
            if target - num in nums and nums.index(target - num) != index:
                return [index, nums.index(target - num)]


obj = Solution()
print(obj.twoSum([3,3], 6))
