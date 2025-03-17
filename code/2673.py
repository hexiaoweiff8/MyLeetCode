class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        def dfs(i):
            if i * 2 >= n:
                return cost[i - 1]
            leftVal = dfs(i * 2)
            rightVal = dfs(i * 2 + 1)
            self.ret += abs(leftVal - rightVal)
            return cost[i - 1] + max(leftVal, rightVal)

        self.ret = 0
        dfs(1)
        return self.ret


obj = Solution()
# print(obj.minIncrements(n=7, cost=[1, 5, 2, 2, 3, 3, 1]))
print(obj.minIncrements(n=15,
                        cost=[764, 1460, 2664, 764, 2725, 4556, 5305, 8829, 5064, 5929, 7660, 6321, 4830, 7055, 3761]))
