from collections import Counter


class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        cnt = Counter([i % value for i in nums])
        mex = 0
        while cnt[mex % value] > 0:
            cnt[mex % value] -= 1
            mex += 1
        return mex


obj = Solution()
print(obj.findSmallestInteger([1,-10,7,13,6,8], 7))
