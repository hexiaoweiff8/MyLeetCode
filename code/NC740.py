class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for num in nums:
            total[num] += num
        def rob(nums2):
            size = len(nums2)
            i, j = nums2[0], max(nums2[0], nums2[1])
            for k in range(2, size):
                i, j = j, max(j, i + nums2[k])
            return j
        return rob(total)