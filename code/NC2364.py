from collections import defaultdict, Counter


class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        cnt = Counter()
        for i, x in enumerate(nums):
            ans += i - cnt[i - x]
            cnt[i - x] += 1
        return ans


obj = Solution()
print(obj.countBadPairs([4, 1, 3, 3]))