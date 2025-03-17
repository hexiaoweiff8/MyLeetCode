class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        target = len(nums) - k + 1
        ret = [0] * target
        left, right = 0, k - 1
        while right < target:
            if right - left < k - 1:
                right += 1
                if nums[right] < nums[right - 1]:
                    for i in range(left, right):
                        ret[i] = -1
                    left = right
            else:
                if nums[right] < nums[right + 1]:
                    ret[left + 1] = max(nums[left + 1:right + 1])
                    right += 1
                    left += 1
                else:
                    for i in range(left + 1, right):
                        ret[i] = -1
                    left = right + 1


        return ret