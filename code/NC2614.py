n = 4000000
prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1
prime[0], prime[1] = False, False  # 0 和 1 不是质数

class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        maxPrime = 0
        for i in range(len(nums)):
            if prime[nums[i][i]]:
                maxPrime = max(maxPrime, nums[i][i])
        for i in range(len(nums)):
            if prime[nums[i][len(nums)-1-i]]:
                maxPrime = max(maxPrime, nums[i][len(nums)-1-i])

        return maxPrime