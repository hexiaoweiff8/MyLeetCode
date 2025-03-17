from sortedcontainers import SortedList


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        list = SortedList(key=lambda x: (x[1], x[2]))
        allTime, time = sum(task[1] for task in tasks), tasks[0][0]
        while tasks:
            while tasks and time >= tasks[0][0]:
                task = tasks.pop(0)
                list.add(task)
            if list:
                enterTime, scope, index = list.pop(0)
                ret.append(index)
                time += scope
            else:
                task = tasks.pop(0)
                ret.append(task[2])
                time = task[0] + task[1]
        while list:
            enterTime, scope, index = list.pop(0)
            ret.append(index)
        return ret


obj = Solution()
# print(obj.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
# print(obj.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
print(obj.getOrder([[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]]))
