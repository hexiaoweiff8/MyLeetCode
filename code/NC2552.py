class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        great = [0] * n
        great[-1] = [0] * (n + 1)
        for i in range(n - 2, 1, -1):
            great[i] = great[i + 1][:]
            for x in range(1, nums[i + 1]):
                great[i][x] += 1
        ret = 0
        less = [0] * (n + 1)
        for j in range(1, n - 1):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    ret += less[nums[k]] * great[k][nums[j]]
        return ret