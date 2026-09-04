class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        minVals = [999999] * n
        minVals[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            minVals[i] = min(minVals[i + 1], nums[i])

        preMax = 0
        for i, x in enumerate(nums):
            preMax = max(preMax, x)
            if preMax - minVals[i] <= k:
                return i
        return -1




obj = Solution()
# print(obj.firstStableIndex([5, 0, 1, 4], 3))
# print(obj.firstStableIndex([3, 2, 1], 1))
# print(obj.firstStableIndex([1, 1], 0))
print(obj.firstStableIndex([6, 1, 4], 5))
