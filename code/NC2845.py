
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        ans = 0
        cnt = [0] * min(modulo, len(nums) + 1)
        preArray = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            preArray[i] += (nums[i - 1] % modulo == k) + preArray[i - 1]
        for x in preArray:
            if x >= k:
                ans += cnt[(x - k) % modulo]
            cnt[x % modulo] += 1
        return ans


obj = Solution()
print(obj.countInterestingSubarrays(nums=[3, 2, 4], modulo=2, k=1))
# print(obj.countInterestingSubarrays(nums=[3, 1, 9, 6], modulo=3, k=0))
