class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            nums.sort(reverse=True)
            return nums
        ret = []
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
                if nums[index]:
                    ret.append(nums[index])
            elif nums[index]:
                ret.append(nums[index])
        if nums[-1]:
            ret.append(nums[-1])
        ret.extend([0 for _ in range(len(nums) - len(ret))])
        return ret


obj = Solution()
# print(obj.applyOperations([1,2,2,1,1,0]))
# print(obj.applyOperations([0,1]))
print(obj.applyOperations([847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]))
