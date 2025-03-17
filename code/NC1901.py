class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        left, right = 0, len(mat) - 2
        while left <= right:
            mid = (left + right) // 2
            mx = max(mat[mid])
            if mx > mat[mid + 1][mat[mid].index(mx)]:
                right = mid - 1
            else:
                left = mid + 1
        return [left, mat[left].index(max(mat[left]))]



obj = Solution()
# print(obj.findPeakGrid([[41, 8, 2, 48, 18],
#                         [16, 15, 9, 7, 44],
#                         [48, 35, 6, 38, 28],
#                         [3, 2, 14, 15, 33],
#                         [39, 36, 13, 46, 42]]))
print(obj.findPeakGrid([[30,41,24,11,24],
                        [23,14,43,18,45],
                        [44,42,5,39,41],
                        [11,35,47,16,11],
                        [30,25,18,41,45]]))
