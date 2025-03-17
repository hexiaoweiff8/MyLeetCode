from collections import defaultdict, Counter


class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # cnt = defaultdict(int)
        # for num1 in nums1:
        #     if num1 % k:
        #         continue
        #     num1 //= k
        #     for d in range(1, int(num1 ** 0.5) + 1):
        #         if num1 % d:
        #             continue
        #         cnt[d] += 1
        #         if d * d < num1:
        #             cnt[num1 // d] += 1
        # return sum(cnt[x] for x in nums2)
        cnt1 = Counter(x // k for x in nums1 if x % k == 0)
        if not cnt1:
            return 0
        ret = 0
        u = max(cnt1)
        for x, cnt in Counter(nums2).items():
            s = sum(cnt1[i] for i in range(x, u + 1, x))
            ret += cnt * s
        return ret
