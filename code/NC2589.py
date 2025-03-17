class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[0])
        maxEnd = max(tasks, key=lambda x: x[1])[1]
        overList = [[] for _ in range(maxEnd + 1)]
        ans = 0
        for i in range(len(tasks)):
            for j in range(tasks[i][0], tasks[i][1] + 1):
                print(j)
                overList[j].append(i)

        for i in range(maxEnd):
            if overList[i]:
                ans += 1
        return ans


obj = Solution()
print(obj.findMinimumTime([[2, 3, 1], [4, 5, 1], [1, 5, 2]]))
