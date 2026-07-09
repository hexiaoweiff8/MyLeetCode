class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        id = [0] * n
        for i in range(n):
            id[i] = id[i - 1]
            if nums[i] - nums[i - 1] > maxDiff:
                id[i] += 1

        return [id[u] == id[v] for u, v in queries]


obj = Solution()
print(obj.pathExistenceQueries(n=2, nums=[569,10949], maxDiff=56389, queries=[[0,0],[1,0]]))
