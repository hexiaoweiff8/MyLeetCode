class Solution(object):
    def findKOr(self, nums, k):
        count = [0] * 32
        for num in nums:
            i = 0
            while num:
                count[i] += num & 1
                num >>= 1
                i += 1
        ret = 0
        isStart = False
        for i in range(31, -1, -1):
            if isStart:
                ret <<= 1
            if count[i] >= k:
                ret += 1
                isStart = True

        return ret


    def findKOr2(self, nums, k):
        ret = 0
        for i in range(31):
            cnt = sum(1 for num in nums if ((num >> i) & 1) > 0)
            if cnt >= k:
                ret |= 1 << i

        return ret


obj = Solution()
print(obj.findKOr([7,12,9,8,9,15], 4))