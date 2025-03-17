class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sortedUnionNums = sorted((set(nums)))
        sortedLen = len(sortedUnionNums)
        ret = n
        j = 0
        for i, left in enumerate(sortedUnionNums):
            right = left + n - 1
            while j < sortedLen and sortedUnionNums[j] <= right:
                ret = min(ret, n - (j - i + 1))
                j += 1
        return ret
