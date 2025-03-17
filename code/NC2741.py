class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            if i == 0 or nums[i] != nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[0]
                nums[0] = tmp
                cnt += 1

        return cnt
