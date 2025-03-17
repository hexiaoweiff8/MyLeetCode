class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp0, dp1, ret = arr[0], 0, arr[0]
        for index in range(1, len(arr)):
            dp1 = max(dp0, dp1 + arr[index])
            dp0 = max(dp0, 0) + arr[index]
            ret = max(dp1, dp0, ret)
        return ret


obj = Solution()
print(obj.maximumSum([1,-2,0,3]))
print(obj.maximumSum([1,-2,-2,3]))
print(obj.maximumSum([-1,-1,-1,-1]))
print(obj.maximumSum([-50]))
print(obj.maximumSum([2,9,-4,7,-6,5,8,-5,-6,9]))