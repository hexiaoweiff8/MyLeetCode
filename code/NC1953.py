class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        # 耗时最长工作所需周数
        longest = max(milestones)
        # 其余工作共计所需周数
        rest = sum(milestones) - longest
        if longest > rest + 1:
            # 此时无法完成所耗时最长的工作
            return rest * 2 + 1
        else:
            # 此时可以完成所有工作
            return longest + rest


obj = Solution()
# print(obj.numberOfWeeks([1, 2, 3]))
# print(obj.numberOfWeeks([5, 2, 1]))
print(obj.numberOfWeeks([1000000000]))
