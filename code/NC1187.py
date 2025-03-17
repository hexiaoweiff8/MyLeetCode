from bisect import bisect_right


class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr2 = sorted(set(arr2))
        n, m = len(arr1), len(arr2)
        dp = [[99999999999] * (min(n, m) + 1) for _ in range(n + 1)]
        dp[0][0] = -1
        for i in range(1, n + 1):
            for j in range(min(i, m) + 1):
                if arr1[i - 1] > dp[i - 1][j]:
                    dp[i][j] = arr1[i - 1]
                if j and dp[i - 1][j - 1] != 99999999999:
                    k = bisect_right(arr2, dp[i - 1][j - 1], j - 1)
                    if k < m:
                        dp[i][j] = min(dp[i][j], arr2[k])
                    if i == n and dp[i][j] != 99999999999:
                        return j
        return -1


obj = Solution()
print(obj.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1]))
