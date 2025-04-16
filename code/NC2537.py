from collections import Counter


class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        index = 0
        cur = 0
        dic = Counter()
        for x in nums:
            cur += dic[x]
            dic[x] += 1
            while cur - dic[nums[index]] + 1 >= k:
                dic[nums[index]] -= 1
                cur -= dic[nums[index]]
                index += 1
            if cur >= k:
                ret += index + 1

        return ret
