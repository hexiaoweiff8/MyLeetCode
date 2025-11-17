class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        preIndex = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if preIndex != -1 and i - preIndex - 1 < k:
                    return False
                preIndex = i

        return True
