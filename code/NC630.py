import heapq


class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])
        sumDur = 0
        queue = []
        for i in range(len(courses)):
            if sumDur + courses[i][0] <= courses[i][1]:
                sumDur += courses[i][0]
                heapq.heappush(queue, -courses[i][0])
            elif queue and -queue[0] > courses[i][0]:
                sumDur -= -queue[0] - courses[i][0]
                heapq.heappop(queue)
                heapq.heappush(queue, -courses[i][0])
        return len(queue)


obj = Solution()
print(obj.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(obj.scheduleCourse([[1, 2]]))
print(obj.scheduleCourse([[3, 2], [4, 3]]))
