class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        ret = 0
        min_val = float('inf')
        max_val = float('-inf')
        for array in arrays:
            ret = max(ret, array[-1] - min_val, max_val - array[0])
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        return ret


obj = Solution()
print(obj.maxDistance([[1, 4], [0, 5]]))
