class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        d = {v: i for i, v in enumerate(arr)}
        f = [1] * len(arr)
        for i, a in enumerate(arr):
            for j in range(i):
                if a % arr[j] == 0 and a // arr[j] in d:
                    f[i] += f[j] * f[d[a // arr[j]]]
        return sum(f) % (10 ** 9 + 7)


obj = Solution()
print(obj.numFactoredBinaryTrees(arr=[2, 4]))
print(obj.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))
