class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        cnt = Counter(nums)
        for x, c in cnt.items():
            if x - k in cnt:
                continue
            f0, f1 = 1, 1 << c
            x += k
            while x in cnt:
                f0, f1 = f1, f1 + f0 * ((1 << cnt[x]) - 1)
                x += k
            ans *= f1
        return ans - 1



obj = Solution()
print(obj.beautifulSubsets([2, 4, 6], 2))