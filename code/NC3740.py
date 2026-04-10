class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has = {}
        minVal = 9999999
        for i, num in enumerate(nums):
            cnt = 0
            idxs = []
            if num in has:
                cnt, idxs = has[num]
                if cnt >= 2:
                    minVal = min(minVal, abs(i - idxs[-1]) + abs(idxs[-2] - idxs[-1]) + abs(i - idxs[-2]))
            has[num] = [cnt + 1, idxs + [i]]
        return -1 if minVal == 9999999 else minVal
