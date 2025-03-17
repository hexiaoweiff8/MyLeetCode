class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        reRes, res = [], []
        ret = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            res.append(len(dic))
        dic = {}
        reRes.append(0)
        for index in range(len(nums) - 1, 0, -1):
            num = nums[index]
            dic[num] = dic.get(num, 0) + 1
            reRes.append(len(dic))
        for i in range(len(nums)):
            ret.append(res[i] - reRes[len(nums) - 1 - i])
        return ret


obj = Solution()
print(obj.distinctDifferenceArray([1, 2, 3, 4, 5]))
print(obj.distinctDifferenceArray([3, 2, 3, 4, 2]))
