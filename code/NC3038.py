class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxAns = 0
        for i in range(len(nums)):
            sumVal = nums[i] + nums[-1]
            ans = 1
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == sumVal:
                    ans += 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > sumVal:
                    right -= 1
                else:
                    left += 1

            maxAns = max(ans, maxAns)

        return maxAns


obj = Solution()
# print(obj.maxOperations([3,2,1,4,5]))
print(obj.maxOperations([3,2,6,1,4]))