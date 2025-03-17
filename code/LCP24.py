from heapq import heappushpop, heappush


class Solution(object):
    def numsGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mod = 10**9 + 7
        ret = [0] * len(nums)
        left = []
        right = []
        left_sum = right_sum = 0
        for i, b in enumerate(nums):
            b -= i
            if i % 2 == 0:
                left_sum -= max(-left[0] - b, 0) if left else 0
                t = -heappushpop(left, -b)
                right_sum += t
                heappush(right, t)
                ret[i] = (right_sum - right[0] - left_sum) % mod
            else:
                right_sum -= max(b - right[0], 0)
                t = heappushpop(right, b)
                left_sum += t
                heappush(left, -t)
                ret[i] = (right_sum - left_sum) % mod
        return ret


        MOD = 1_000_000_007
        ans = [0] * len(nums)
        left = []   # 维护较小的一半，大根堆（小根堆取负号）
        right = []  # 维护较大的一半，小根堆
        left_sum = right_sum = 0
        for i, b in enumerate(nums):
            b -= i
            if i % 2 == 0:  # 前缀长度是奇数
                left_sum -= max(-left[0] - b, 0) if left else 0
                t = -heappushpop(left, -b)
                right_sum += t
                heappush(right, t)
                ans[i] = (right_sum - right[0] - left_sum) % MOD
            else:  # 前缀长度是偶数
                right_sum += max(b - right[0], 0)
                t = heappushpop(right, b)
                left_sum += t
                heappush(left, -t)
                ans[i] = (right_sum - left_sum) % MOD
        return ans


obj = Solution()
print(obj.)