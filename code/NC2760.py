class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        arrayLen = maxLen = 0
        preIsSingle = True
        for num in nums:
            if num <= threshold:
                if num % 2 == 0 and preIsSingle:
                    arrayLen += 1
                    preIsSingle = False
                elif num % 2 == 1 and not preIsSingle:
                    arrayLen += 1
                    preIsSingle = True
                else:
                    maxLen = max(maxLen, arrayLen)
                    arrayLen = 0 if num % 2 == 1 else 1
                    preIsSingle = True if num % 2 == 1 else False
            else:
                maxLen = max(maxLen, arrayLen)
                arrayLen = 0
                preIsSingle = True
        return max(maxLen, arrayLen)


obj = Solution()
# print(obj.longestAlternatingSubarray([4, 10, 3], 10))
print(obj.longestAlternatingSubarray([8, 10, 7, 8, 3], 9))
