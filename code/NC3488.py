import bisect


class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = []
        n = len(nums)
        for i, num in enumerate(nums):
            indexList = dic.get(num, [])
            indexList.append(i)
            dic[num] = indexList
        for lst in dic.values():
            x = lst[0]
            lst.insert(0, lst[-1] - n)
            lst.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = dic[x]
            if len(pos_list) == 3:
                ans.append(-1)
                continue
            pos = bisect.bisect_left(pos_list, queries[i])
            print(pos)
            ans.append(min(pos_list[pos + 1] - pos_list[pos], pos_list[pos] - pos_list[pos - 1]))

        return ans


obj = Solution()
print(obj.solveQueries([14,14,4,2,19,19,14,19,14], [2,4,8,6,3]))
