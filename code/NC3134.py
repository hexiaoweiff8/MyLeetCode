import bisect
from collections import defaultdict


class Solution(object):
    def medianOfUniquenessArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def check(upper):
            cnt = l = 0
            freq = defaultdict(int)
            for r, in_ in enumerate(nums):
                freq[in_] += 1
                while len(freq) > upper:
                    out = nums[l]
                    freq[out] -= 1
                    if freq[out] == 0:
                        del freq[out]
                    l += 1
                cnt += r - l + 1
                if cnt >= k:
                    return True

            return False
        return bisect.bisect_left(range(len(set(nums))), True, 1, key=check)