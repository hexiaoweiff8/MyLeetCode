class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for index in range(1, len(nums)):
            nums[index] = nums[index - 1] + nums[index]

        for index in range(len(queries)):
            query = queries[index]
            if query < nums[0]:
                queries[index] = 0
            elif query >= nums[-1]:
                queries[index] = len(nums)
            else:
                for index2, num in enumerate(nums):
                    if num > query:
                        queries[index] = index2
                        break

        return queries
        # sortNums = list(accumulate(nums))
        # return [bisect.bisect_right(sortNums, q) for q in queries]


obj = Solution()
print(obj.answerQueries([4,5,2,1], [3,10,21]))