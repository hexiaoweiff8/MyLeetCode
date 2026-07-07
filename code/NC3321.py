from collections import defaultdict
from sortedcontainers import SortedList

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 使用SortedList维护(-频率, -값)的有序列表
        sorted_list = SortedList()
        # 使用字典记录每个数字的频率
        freq = defaultdict(int)
        ans = []
        
        # 初始化前k个元素
        for i in range(k):
            # 更新频率并添加新的(-频率, -값)对
            freq[nums[i]] += 1
            sorted_list.add((-freq[nums[i]], -nums[i]))
        
        # 处理第一个窗口
        sum_val = 0
        for i in range(min(x, len(sorted_list))):
            neg_freq, neg_val = sorted_list[i]
            freq_val, val = -neg_freq, -neg_val
            sum_val += val * freq_val
        ans.append(sum_val)
        
        # 滑动窗口处理后续元素
        for i in range(k, len(nums)):
            # 移除窗口左边的元素
            if freq[nums[i-k]] > 0:
                sorted_list.remove((-freq[nums[i-k]], -nums[i-k]))
            freq[nums[i-k]] -= 1
            # 如果频率仍大于0，重新添加
            if freq[nums[i-k]] > 0:
                sorted_list.add((-freq[nums[i-k]], -nums[i-k]))
            
            # 添加窗口右边的新元素
            if freq[nums[i]] > 0:
                sorted_list.remove((-freq[nums[i]], -nums[i]))
            freq[nums[i]] += 1
            sorted_list.add((-freq[nums[i]], -nums[i]))
            
            # 计算当前窗口的x-sum
            sum_val = 0
            for j in range(min(x, len(sorted_list))):
                neg_freq, neg_val = sorted_list[j]
                freq_val, val = -neg_freq, -neg_val
                sum_val += val * freq_val
            ans.append(sum_val)
        
        return ans

obj = Solution()
print(obj.findXSum([1,1,2,2,3,4,2,3], 6, 2))
