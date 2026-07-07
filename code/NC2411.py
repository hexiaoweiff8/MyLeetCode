class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            pre[i] = nums[i] | pre[i + 1]
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i, len(nums)):
                if pre[i] == val:
                    ans.append(j - i + 1)
                    break
                val |= nums[j]

        return ans


obj