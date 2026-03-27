class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n, m = len(mat), len(mat[0])
        if k > m:
            k = k % m

        for i in range(n):
            if i % 2 == 0:
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False
            else:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
        return True


obj = Solution()
print(obj.areSimilar([[2, 2], [25, 23]], 35))
