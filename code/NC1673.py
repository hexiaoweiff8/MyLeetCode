class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and len(nums) - i > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack