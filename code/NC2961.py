class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(variables)):
            print((((variables[i][0] ** variables[i][1]) % 10) ** variables[i][2]) % variables[i][3])
            if (((variables[i][0] ** variables[i][1]) % 10) ** variables[i][2]) % variables[i][3] == target:
                ans.append(i)
        return ans


obj = Solution()
print(obj.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2))