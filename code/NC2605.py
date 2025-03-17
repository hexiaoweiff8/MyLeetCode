class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        minNum1 = float("inf")
        for num1 in nums1:
            if num1 in nums2:
                minNum1 = min(minNum1, num1)
        if minNum1 != float("inf"):
            return minNum1
        minNum2 = min(nums2)
        minNum1 = min(nums1)
        return min(minNum1, minNum2) * 10 + max(minNum1, minNum2)


obj = Solution()
print(obj.minNumber(nums1 = [4,1,3], nums2 = [5,7]))
print(obj.minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))