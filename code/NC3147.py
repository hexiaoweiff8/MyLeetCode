class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0] * n
        dp[n - 1] = energy[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = energy[i] + dp[i + k] if i + k < n else energy[i]
        return max(dp)
