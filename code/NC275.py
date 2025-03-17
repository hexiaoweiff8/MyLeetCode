class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0
        for index in range(len(citations) - 1, -1, -1):
            if count + 1 <= citations[index] and citations[index] > 0:
                count += 1
        return count

    def hIndex2(self, citations):
        # 二分查找
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left



obj = Solution()
print(obj.hIndex([0, 1, 3, 5, 6]))
print(obj.hIndex([1, 2, 100]))
print(obj.hIndex([1]))
print(obj.hIndex([0]))
print(obj.hIndex([1, 1]))
