class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        numsLen = len(nums)
        coupleCount = 0
        for num in nums:
            count = dic.get(num, 0) + 1
            dic[num] = count

        for key, count in dic.items():
            coupleCount += count // 2

        return [coupleCount, numsLen - coupleCount * 2]

obj = Solution()
print(obj.numberOfPairs([1,3,2,1,3,2,2]))
