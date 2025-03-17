class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        res1, res2 = 0, 0
        last2, last1 = max(nums1[-1], nums2[-1]), min(nums1[-1], nums2[-1])
        for i in range(n):
            if last1 >= nums1[i] and last1 >= nums2[i]:
                pass
            elif last1 >= nums1[i] and last2 >= nums2[i]:
                res2 += 1
            elif last2 >= nums2[i] and last2 >= nums1[i]:
                res1 += 1
            else:
                return -1
        return min(res1, res2)


obj = Solution()
# print(obj.minOperations(nums1=[1, 2, 7], nums2=[4, 5, 3]))
# print(obj.minOperations(nums1=[1, 2], nums2=[2, 1]))
print(obj.minOperations(nums1=[8, 6, 6, 6, 7, 8],
                        nums2=[5, 8, 8, 8, 7, 7]))
