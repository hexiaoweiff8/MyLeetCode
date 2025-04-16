class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dic1, dic2 = {}, {}
        for i, num in enumerate(nums1):
            dic1[num] = i
        for i, num in enumerate(nums2):
            dic2[num] = i
        ans = 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                for k in range(j + 1, len(nums1)):
                    if dic1[nums1[i]] < dic1[nums1[j]] < dic1[nums1[k]] and dic2[nums1[i]] < dic2[nums1[j]] < dic2[nums1[k]]:
                        ans += 1

        return ans