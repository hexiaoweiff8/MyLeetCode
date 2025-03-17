class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1] <= heights[i]:
                res[i] += 1
                stack.pop()
            if stack:
                res[i] += 1
            stack.append(heights[i])
        return res