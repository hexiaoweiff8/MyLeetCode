class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = delete = s.count("a")
        for char in s:
            delete -= 1 if char == "a" else -1
            if delete < count:
                count = delete
        return count

        # 动态规划
    def dy(self, s):
        f = countB = 0
        for char in s:
            if char == "b":
                countB += 1
            else:
                f = min(f + 1, countB)
        return f


obj = Solution()
print(obj.minimumDeletions("aababbab"))
print(obj.minimumDeletions("bbaaaaabb"))
