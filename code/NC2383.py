class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        # 计算前缀和差值最大的返回
        sumEx = initialExperience
        sumEn = sum(energy)
        sumEnHours = 0
        if sumEn >= initialEnergy:
            sumEnHours = sumEn - initialEnergy + 1
        sumnExHours = 0
        if experience[0] >= initialExperience:
            sumnExHours = experience[0] - initialExperience + 1
            sumEx += sumnExHours
        sumEx += experience[0]
        for index in range(1, len(energy)):
            if experience[index] >= sumEx:
                sumnExHours += max(0, experience[index] - sumEx + 1)
                sumEx = experience[index] + 1
            sumEx += experience[index]

        return sumEnHours + sumnExHours


obj = Solution()
# print(obj.minNumberOfHours(2, 4, [1], [3]))
# print(obj.minNumberOfHours(5, 3, [1,4,3,2], [2,6,3,1]))
# print(obj.minNumberOfHours(1, 1,[1,1,1,1],[1,1,1,50]))
print(obj.minNumberOfHours(5, 1, [1,3,3], [1,3,7]))