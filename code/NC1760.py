class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            ops = sum((num - 1) // mid for num in nums)
            if ops > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left
