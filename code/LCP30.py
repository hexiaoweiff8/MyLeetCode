from sortedcontainers import SortedList


class Solution(object):
    def magicTower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < 0:
            return - 1
        ret = 0
        hp = 1
        stack = SortedList()
        for i in range(len(nums)):
            if nums[i] < 0:
                stack.add(nums[i])
                if hp + nums[i] <= 0:
                    ret += 1
                    hp -= stack.pop(0)
            hp += nums[i]
        return ret


obj = Solution()
print(obj.magicTower([100, 100, 100, -250, -60, -140, -50, -50, 100, 150]))
# print(obj.magicTower([-200, -300, 400, 0]))
# print(obj.magicTower([5, -4, 1, -2, -2, -2, 4]))
