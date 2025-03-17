class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        numsLen = len(nums)
        for index, num in enumerate(nums):
            hasVal = False
            for index2 in range(index + 1, numsLen):
                if hasVal:
                    break
                if num < nums[index2]:
                    for index3 in range(index2 + 1, numsLen):
                        if num < nums[index3]:
                            ret.append(nums[index3])
                            hasVal = True
                            break
            if not hasVal:
                ret.append(-1)
        return ret


obj = Solution()
print(obj.secondGreaterElement([2,4,0,9,6]))
print(obj.secondGreaterElement([3,3]))