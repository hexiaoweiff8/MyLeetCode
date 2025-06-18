class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            # 如三个值中任意两个值差值超过k, 则返回空数组
            if abs(nums[i] - nums[i + 2]) > k:
                return []
            ans.append(nums[i:i+3])

        return ans