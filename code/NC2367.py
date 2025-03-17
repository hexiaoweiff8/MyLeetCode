class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        ret = 0
        for num in nums:
            if num + diff in nums and num + diff * 2 in nums:
                ret += 1
        return ret


obj = Solution()
print(obj.arithmeticTriplets([4,5,6,7,8,9], 2))