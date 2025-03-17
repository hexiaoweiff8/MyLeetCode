class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenNums1 = len(nums1)
        lenNums2 = len(nums2)
        forLen = (lenNums1 + lenNums2) // 2
        isDouble = (lenNums1 + lenNums2) % 2 == 0
        index1 = 0
        index2 = 0
        val = 0
        preVal = 0
        while index1 + index2 <= forLen:
            preVal = val
            if index2 < lenNums2 and (index1 >= lenNums1 or nums1[index1] > nums2[index2]):
                val = nums2[index2]
                index2 += 1
            else:
                val = nums1[index1]
                index1 += 1

        if isDouble:
            return (val + preVal) / 2.0
        else:
            return val

        # -------------蛋疼--------------
        # allNums = nums1 + nums2
        # allNums.sort()
        # lenAllNums = len(allNums)
        # mid = int(lenAllNums / 2)
        # isDouble = lenAllNums % 2 == 0
        # if isDouble:
        #     return (allNums[mid] + allNums[mid - 1]) / 2.0
        # else:
        #     return allNums[mid]

obj = Solution()
print(obj.findMedianSortedArrays([1,2], [3,4]))
