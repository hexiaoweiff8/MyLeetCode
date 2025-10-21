import collections


class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        diff = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        ans = 0
        cur = 0
        for x in sorted(diff.keys()):
            cur += diff[x]
            ans = max(ans, min(cur, cnt[x] + numOperations))
        return ans

obj = Solution()
print(obj.maxFrequency([88, 53], 28, 2))
