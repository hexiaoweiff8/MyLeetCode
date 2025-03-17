class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        m = len(nums)
        for i in range(m):
            for j in range(i + 1, m):
                diff = nums[j] - nums[i]
                cur = 2
                for k in range(j + 1, m):
                    if nums[k] - nums[j] == diff:
                        cur += 1
                        j = k
                ans = max(ans, cur)

        return ans