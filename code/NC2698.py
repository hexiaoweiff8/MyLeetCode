class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(s, pos, tot, target):
            if pos == len(s):
                return tot == target
            sum = 0
            for i in range(pos, len(s)):
                sum = sum * 10 + int(s[i])
                if sum + tot > target:
                    break
                if dfs(s, i + 1, tot + sum, target):
                    return True
            return False
        res = 0
        for i in range(1, n + 1):
            if dfs(str(i * i), 0, 0, i):
                res += i * i
        return res


obj = Solution()
print(obj.punishmentNumber(10))
print(obj.punishmentNumber(37))
