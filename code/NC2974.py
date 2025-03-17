class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        while len(nums) > 1:
            min1 = min(nums)
            nums.remove(min1)
            min2 = min(nums)
            nums.remove(min2)
            arr.append(min2)
            arr.append(min1)

        if len(nums) == 1:
            arr.append(nums[0])
        return arr