from collections import defaultdict, Counter


class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        startList = nums[:k]
        dic = defaultdict(int)
        ans = []
        for i in startList:
            dic[i] += 1
        for i in range(k, len(nums)):
            # 获取dic中count最大的x个key 如果数量相同则取最大的key
            # 先排序 数量相同则取最大的key
            cnt = sorted(Counter(dic).items(), key=lambda x: (x[1], x[0]), reverse=True)
            ans.append(sum([i[0] * i[1] for i in cnt[:x]]))
            dic[nums[i]] += 1
            dic[nums[i - k]] -= 1

        cnt = sorted(Counter(dic).items(), key=lambda x: (x[1], x[0]), reverse=True)
        ans.append(sum([i[0] * i[1] for i in cnt[:x]]))
        return ans

obj = Solution()
print(obj.findXSum([1,1,2,2,3,4,2,3], 6, 2))
