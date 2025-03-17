class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        # 排序 使用二分法处理数据
        lenNums = len(nums)
        nums.sort()
        count = 0
        for index1 in range(lenNums):
            for index2 in range(index1 + 1, lenNums):
                if low <= nums[index1] ^ nums[index2] <= high:
                    count += 1

        return count


obj = Solution()
print(obj.countPairs([9, 8, 4, 2, 1], 5, 14))
