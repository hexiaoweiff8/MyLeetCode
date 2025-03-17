from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        return [key for key, val in counter.items() if val == 1]


obj = Solution()
print(obj.singleNumber([1, 2, 1, 3, 2, 5]))
print(obj.singleNumber([-1, 0]))
print(obj.singleNumber([0, 1]))
