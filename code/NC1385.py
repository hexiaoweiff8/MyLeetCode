class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr1.sort()
        arr2.sort()
        ans = j = 0
        for arr1Num in arr1:
            while j < len(arr2) and arr2[j] < arr1Num - d:
                j += 1
            if j == len(arr2) or arr2[j] > arr1Num + d:
                ans += 1
        return ans