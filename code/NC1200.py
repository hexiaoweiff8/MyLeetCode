class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        minDiff = min([arr[i+1] - arr[i] for i in range(len(arr)-1)])
        return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == minDiff]