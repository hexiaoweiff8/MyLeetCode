class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                for i in range(1, 32):
                    if num >> i & 1 ^ 1:
                        ans.append(num ^ 1 << (i - 1))
                        break
        return ans