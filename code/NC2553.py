class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            subArray = []
            while num:
                subArray.insert(0, num % 10)
                num //= 10
            ans += subArray

        return ans