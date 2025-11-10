class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num == 0:
                continue
            if not stack or stack[-1] < num:
                stack.append(num)
                ans += 1
        return ans
