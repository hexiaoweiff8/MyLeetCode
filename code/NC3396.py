import collections


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        counter = collections.Counter(nums)
        res = index = 0
        for num in nums:
            # 查询counter中所有数值是否有大于1的
            if counter.values().count(1) == n - index:
                break
            counter[num] -= 1
            index += 1
            if index % 3 == 0:
                res += 1
        if index % 3 != 0:
            res += 1
        return res

    def minimumOperations2(self, nums):
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0


obj = Solution()
print(obj.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
