
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxVal = max(nums)
        ans = 0
        left = 0
        maxCnt = 0
        for num in nums:
            if maxVal == num:
                maxCnt += 1
            while maxCnt == k:
                if nums[left] == maxVal:
                    maxCnt -= 1
                left += 1
            ans += left
        return ans


obj = Solution()
print(obj.countSubarrays([1, 3, 2, 3, 3], 2))
