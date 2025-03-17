from collections import Counter


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        ret = 0
        n = len(nums)
        t = 0
        for index, value in count.items():
            ret += t * value * (n - t - value)
            t += value
        return ret


obj = Solution()
# print(obj.unequalTriplets([4,4,2,4,3]))
# print(obj.unequalTriplets([1,1,1,1,1]))
print(obj.unequalTriplets([1,3,1,2,4]))