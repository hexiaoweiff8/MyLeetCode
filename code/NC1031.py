class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == firstLen + secondLen:
            return sum(nums)
        return max(self.check(nums, firstLen, secondLen), self.check(nums, secondLen, firstLen))

    def check(self, nums, firstLen, secondLen):
        sumL = 0
        for index in range(0, firstLen):
            sumL += nums[index]
        maxSumL = sumL
        sumR = 0
        for index in range(firstLen, firstLen + secondLen):
            sumR += nums[index]
        ret = maxSumL + sumR
        index2 = firstLen
        for index in range(firstLen + secondLen, len(nums)):
            sumL += nums[index2] - nums[index2 - firstLen]
            maxSumL = max(maxSumL, sumL)
            sumR += nums[index] - nums[index - secondLen]
            ret = max(ret, maxSumL + sumR)
            index2 += 1
        return ret


obj = Solution()
print(obj.maxSumTwoNoOverlap(nums=[0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen=1, secondLen=2))
print(obj.maxSumTwoNoOverlap(nums=[3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen=3, secondLen=2))
print(obj.maxSumTwoNoOverlap(nums=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen=4, secondLen=3))
