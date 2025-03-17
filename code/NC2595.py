class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0, 0]
        for i, c in enumerate(bin(n)[2:][::-1]):
            if i % 2 == 0 and c == '1':
                ans[0] += 1
            if i % 2 == 1 and c == '1':
                ans[1] += 1
        return ans


obj = Solution()
# print(obj.evenOddBit(n=17))
print(obj.evenOddBit(n=2))