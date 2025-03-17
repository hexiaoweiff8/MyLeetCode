class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, m = len(nums), len(str(nums[0]))
        ret = 0
        for _ in range(m):
            dic = [0] * 10
            for index, num in enumerate(nums):
                dic[num % 10] += 1
                nums[index] //= 10
            ret += sum(v * (n - v) for v in dic) // 2

        return ret
