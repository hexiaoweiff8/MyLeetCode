import math


class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def prime(n):
            if n == 1: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        primes = []
        for i in range(len(nums)):
            if prime(nums[i]):
                primes.append(i)
        return primes[-1] - primes[0]
