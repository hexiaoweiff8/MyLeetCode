class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kIndex = -1
        dic = {0: 1}
        diff = 0
        subCount = 0
        for i, num in enumerate(nums):
            if num == k:
                kIndex = i
            elif num > k:
                diff += 1
            else:
                diff -= 1

            if kIndex < 0:
                dic[diff] = dic.get(diff, 0) + 1
            else:
                subCount += dic.get(diff, 0) + dic.get(diff - 1, 0)
        return subCount


obj = Solution()
# print(obj.countSubarrays([3, 2, 1, 4, 5], 4))
# print(obj.countSubarrays([2, 3, 1], 3))
print(obj.countSubarrays([2, 5, 1, 4, 3, 6], 1))
