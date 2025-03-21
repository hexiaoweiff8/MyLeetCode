class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            pre[i] = pre[i + 1] | nums[i]

        ans = 0
        preVal = 0
        for i in range(n):
            ans = max(ans, preVal | (nums[i] << k) | pre[i + 1])
            preVal |= nums[i]
        return ans


obj = Solution()
print(obj.maximumOr(nums=[12,9], k=1))
