from collections import Counter


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        counter = Counter([nums[i] * nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums))])
        for key, value in counter.items():
            res += value * (value - 1) * 4

        return res


obj = Solution()
print(obj.tupleSameProduct([2, 3, 4, 6]))
print(obj.tupleSameProduct([1, 2, 4, 5, 10]))
