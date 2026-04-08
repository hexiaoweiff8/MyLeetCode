class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        for l, r, k, v in queries:
            index = l
            while index <= r:
                nums[index] = (nums[index] * v) % MOD
                index += k
        def xor_all(nums):
            result = 0
            for num in nums:
                result ^= num
            return result
        # 返回所有元素异或结果
        return xor_all(nums)