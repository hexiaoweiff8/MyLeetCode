import collections


class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(set(nums))
        cnt = collections.defaultdict(int)
        ans = left = 0
        for x in nums:
            cnt[x] += 1
            while len(cnt) == k:
                out = nums[left]
                cnt[out] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans

obj = Solution()
# print(obj.countCompleteSubarrays([5, 5, 5, 5]))
print(obj.countCompleteSubarrays([1786, 1786, 1786, 114]))
