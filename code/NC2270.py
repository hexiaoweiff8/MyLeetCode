class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        front = [0]
        for num in nums:
            front.append(front[-1] + num)
        front.pop(0)
        for i in range(len(nums) - 1):
            if front[i] >= front[-1] - front[i]:
                ans += 1
        return ans


obj = Solution()
# print(obj.waysToSplitArray([10, 4, -8, 7]))
print(obj.waysToSplitArray([-2,-1]))