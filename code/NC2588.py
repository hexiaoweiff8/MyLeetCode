class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = Counter()
        cnt[0] = 1
        cur = 0
        for x in nums:
            cur ^= x
            ans += cnt[cur]
            cnt[cur] += 1
        return ans