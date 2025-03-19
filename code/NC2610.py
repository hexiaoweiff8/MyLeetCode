class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        nums.sort()
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
            if dic[i] + 1 > len(res):
                res.append([])
            res[dic[i]].append(i)

        return res


obj = Solution()
print(obj.findMatrix([1, 3, 4, 1, 2, 3, 1]))
