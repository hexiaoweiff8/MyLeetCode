class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += (1 if nums[j] == target else -1)
                if cnt > 0:
                    ans += 1

        return ans