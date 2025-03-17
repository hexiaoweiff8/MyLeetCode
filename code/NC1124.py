class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        lenHours = len(hours)
        maxCount = 0
        scoreList = [0] * (lenHours + 1)
        stk = [0]
        for index in range(1, lenHours + 1):
            scoreList[index] = scoreList[index - 1] + (1 if hours[index - 1] > 8 else -1)
            if scoreList[stk[-1]] > scoreList[index]:
                stk.append(index)

        for index in range(lenHours, 0, -1):
            while stk and scoreList[stk[-1]] < scoreList[index]:
                maxCount = max(maxCount, index - stk[-1])
                stk.pop()

        return maxCount
        # ans = s = 0
        # pos = {}
        # for i, x in enumerate(hours):
        #     s += 1 if x > 8 else -1
        #     if s > 0:
        #         ans = i + 1
        #     elif s - 1 in pos:
        #         ans = max(ans, i - pos[s - 1])
        #     if s not in pos:
        #         pos[s] = i
        # return ans


obj = Solution()
print(obj.longestWPI([8,10,6,16,5]))
print(obj.longestWPI([9,9,6,0,6,6,9]))