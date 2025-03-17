class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        subZero = []
        upZero = []
        subZeroMutil = 1
        ret = 1
        hasZero = False
        for num in nums:
            if num < 0:
                subZero.append(num)
                subZeroMutil *= num
            elif num > 0:
                ret *= num
                upZero.append(num)
            else:
                hasZero = True
        if subZeroMutil < 0:
            subZeroMutil /= max(subZero)
        if len(subZero) <= 1 and len(upZero) == 0 and hasZero:
            return 0

        return ret * subZeroMutil

    def maxStrength2(self, nums):
        mn = mx = nums[0]
        for x in nums[1:]:
            mn, mx = min(mn, x, mn * x, mx * x), \
                max(mx, x, mn * x, mx * x)
        return mx


obj = Solution()
# print(obj.maxStrength([3,-1,-5,2,5,-9]))
# print(obj.maxStrength([0, -1]))
# print(obj.maxStrength([-9]))
# print(obj.maxStrength([-3,0,1]))
print(obj.maxStrength([-1,-1,0]))