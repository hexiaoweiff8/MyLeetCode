class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 将数据恢复成升序
        spartIndex = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                spartIndex = i
                break
        # 进行两次二分查找, 以spartIndex作为分界
        def binarySearch(nums, target, left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        l, r = 0, spartIndex
        res = binarySearch(nums, target, l, r)
        if res != -1:
            return res
        return binarySearch(nums, target, spartIndex + 1, len(nums) - 1)


obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))
