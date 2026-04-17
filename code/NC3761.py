class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        res = n
        last_index = {}
        for i, x in enumerate(nums):
            if x in last_index:
                res = min(res, i - last_index[x])
            rev = int(str(x)[::-1])
            last_index[rev] = i
        return res if res != n else -1


obj = Solution()
print(obj.minMirrorPairDistance([120,21]))
