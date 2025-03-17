class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        for index, char in enumerate(s):
            nums[index] += d if char == "R" else -d
        nums.sort()
        ret = count = 0
        for index, num in enumerate(nums):
            ret += index * num - count
            count += num
        return ret % 10**9 + 7
