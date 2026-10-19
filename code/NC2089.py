class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        for i, v in enumerate(nums):
            if v == target:
                ans.append(i)
        return ans