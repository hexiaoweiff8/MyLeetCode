class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        ans = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    ans.add(j)
        ans = list(ans)
        ans.sort()
        return ans