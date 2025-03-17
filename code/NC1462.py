class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prerequisites.sort(reverse=True, key=lambda x: x[0])
        graph = [[False] * numCourses for _ in range(numCourses)]
        ret = []
        for pre in prerequisites:
            graph[pre[0]][pre[1]] = True
        for i in range(numCourses):
            for j in range(numCourses):
                if not graph[j][i]:
                    continue
                for k in range(numCourses):
                    if graph[i][k]:
                        graph[j][k] = True
        for query in queries:
            ret.append(graph[query[0]][query[1]])
        return ret


obj = Solution()
print(obj.checkIfPrerequisite(numCourses=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))
print(obj.checkIfPrerequisite(numCourses=2, prerequisites=[], queries=[[1, 0], [0, 1]]))
print(obj.checkIfPrerequisite(numCourses=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
print(obj.checkIfPrerequisite(numCourses=5,
                              prerequisites=[[4, 3], [4, 1], [4, 0], [3, 2], [3, 1], [3, 0], [2, 1], [2, 0], [1, 0]],
                              queries=[[1, 4], [4, 2], [0, 1], [4, 0], [0, 2], [1, 3], [0, 1]]))
