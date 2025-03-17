class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = [0, 0]
        for i in nums1:
            if i in nums2:
                ret[0] += 1

        for i in nums2:
            if i in nums1:
                ret[1] += 1

        return ret


obj = Solution()
print(obj.findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]))