class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n = len(skill)
        last_finish = [0] * n
        for m in mana:
            sum_t = 0
            for x, last in zip(skill, last_finish):
                if last > sum_t:
                    sum_t = last
                sum_t += x * m

            last_finish[-1] = sum_t
            for i in range(n - 2, -1, -1):
                last_finish[i] = last_finish[i + 1] - skill[i + 1] * m

        return last_finish[-1]


