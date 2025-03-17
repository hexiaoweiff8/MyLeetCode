class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 获得1和n在nums中的位置
        n = len(nums)
        index1 = nums.index(1)
        indexn = nums.index(n)
        if index1 < indexn:
            return index1 + n - indexn - 1
        else:
            return index1 + n - indexn - 2