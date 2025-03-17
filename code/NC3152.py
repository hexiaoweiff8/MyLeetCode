class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        ans = []
        queryArray = []
        preArray = [0]
        preNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] % 2 != preNum % 2:
                queryArray.append(0)
                preNum = nums[i]
            else:
                queryArray.append(1)
            preArray.append(preArray[i - 1] + queryArray[i - 1])

        for i in range(len(queries)):
            ans.append(preArray[queries[i][1]] - preArray[queries[i][0]] == 0)
        return ans


obj = Solution()
print(obj.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
