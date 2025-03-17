class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        sumVal = 0
        for num in nums:
            if int(num / 3 * 10) % 10 == 0:
                count += 1
                sumVal += num

        if count == 0:
            return 0
        return sumVal / count


obj = Solution()
print(obj.averageValue([1,3,6,10,12,15]))
print(obj.averageValue([1,2,4,7,10]))
