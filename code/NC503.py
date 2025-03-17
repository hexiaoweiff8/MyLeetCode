class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ret = []
        # n = len(nums)
        # for i in range(n):
        #     hasVal = False
        #     for j in range(i + 1, n + i):
        #         j %= n
        #         if nums[j] > nums[i]:
        #             ret.append(nums[j])
        #             hasVal = True
        #             break
        #
        #     if not hasVal:
        #         ret.append(-1)
        #
        # return ret

        n = len(nums)
        ret = [-1] * n
        stack = []
        for i in range(n * 2 - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                ret[stack.pop()] = nums[i % n]
            stack.append(i % n)

        return ret

obj = Solution()
print(obj.nextGreaterElements([1,2,1]))