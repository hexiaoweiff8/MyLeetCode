class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        # 求和
        x = sum(nums) % p
        if x == 0:
            return 0
        y = 0
        dic = {0: -1}
        ret = len(nums)
        for index, val in enumerate(nums):
            y = (y + val) % p
            if (y - x) % p in dic:
                ret = min(ret, index - dic[(y - x) % p])
            dic[y] = index
        return ret if ret < len(nums) else -1


obj = Solution()
print(obj.minSubarray([3,1,4,2], 6))
print(obj.minSubarray([6,3,5,2], 9))
print(obj.minSubarray([1,2,3], 3))
print(obj.minSubarray([1,2,3], 7))
