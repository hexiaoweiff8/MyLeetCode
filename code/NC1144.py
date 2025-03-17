class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 计算单次差值的梯度和
        lenNums = len(nums);
        if lenNums <= 2:
            return 0
        subSumDown = subSumUp = 0
        nums = [nums[1]] + nums + [nums[-2]]
        for index in range(1, len(nums) - 1):
            num = nums[index]
            minVal = min(nums[index - 1], nums[index + 1])
            if index % 2 == 1:
                # 计算down两边最小值-1
                subSumDown += num - minVal + 1 if num >= minVal else 0
            else:
                # 计算up两边最小值-1
                subSumUp += num - minVal + 1 if num >= minVal else 0
        print(subSumDown, subSumUp)
        return min(subSumDown, subSumUp)


obj = Solution()
# print(obj.movesToMakeZigzag([1, 2, 3]))
# print(obj.movesToMakeZigzag([9, 6, 1, 6, 2]))
# print(obj.movesToMakeZigzag([2, 7, 10, 9, 8, 9]))
# print(obj.movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]))
print(obj.movesToMakeZigzag([10, 1]))
