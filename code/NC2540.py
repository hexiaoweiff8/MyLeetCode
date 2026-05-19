class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        index1, index2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while nums1[index1] != nums2[index2]:
            if nums1[index1] > nums2[index2]:
                index2 += 1
            elif nums2[index2] > nums1[index1]:
                index1 += 1
            if index1 >= n1 or index2 >= n2:
                return -1

        return nums1[index1]


obj = Solution()
print(obj.getCommon([1, 2, 3], [2, 4]))
