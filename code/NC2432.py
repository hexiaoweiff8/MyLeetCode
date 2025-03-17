class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        maxScope = 0
        preTime = 0
        maxScopeId = 0
        for log in logs:
            if maxScope < log[1] - preTime:
                maxScope = log[1] - preTime
                maxScopeId = log[0]
            elif maxScope == log[1] - preTime:
                maxScopeId = min(log[0], maxScopeId)
            preTime = log[1]

        return maxScopeId


obj = Solution()
print(obj.hardestWorker(n = 70, logs = [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))
