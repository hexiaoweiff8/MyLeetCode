import heapq


class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # 构建小端堆, 堆顶为最小值
        self.stack = []
        self.removeTasks = {}
        for userId, taskId, priority in tasks:
            self.removeTasks[taskId] = (priority, userId)
            heapq.heappush(self.stack, (-priority, -taskId, userId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.removeTasks[taskId] = (priority, userId)
        heapq.heappush(self.stack, (-priority, -taskId, userId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        self.add(self.removeTasks[taskId][1], taskId, newPriority)

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        self.removeTasks[taskId] = (-1, -1)

    def execTop(self):
        """
        :rtype: int
        """
        while self.stack:
            priority, taskId, userId = heapq.heappop(self.stack)
            if self.removeTasks[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
        return -1



# Your TaskManager object will be instantiated and called as such:
obj = TaskManager([[3,12,11],[6,2,46],[2,1,46],[5,23,21]])
print(obj.execTop())