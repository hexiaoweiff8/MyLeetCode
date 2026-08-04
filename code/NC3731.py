class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = set(nums)
        minV, maxV = min(nums), max(nums)
        return [i for i in range(minV, maxV) if i not in st]
