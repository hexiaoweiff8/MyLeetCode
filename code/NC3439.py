class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        nums = [startTime[0]]
        for i in range(1, len(startTime)):
            nums.append(startTime[i] - endTime[i - 1])
        nums.append(eventTime - endTime[-1])
        ans = s = 0
        for i, x in enumerate(nums):
            s += x
            if i >= k:
                ans = max(ans, s)
                s -= nums[i - k]
        return ans



obj = Solution()
# print(obj.maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
# print(obj.maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(obj.maxFreeTime(eventTime=21, k=2, startTime=[18, 20], endTime=[20, 21]))
