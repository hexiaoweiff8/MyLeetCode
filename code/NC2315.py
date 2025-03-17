class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        isOpen = True
        count = 0
        for char in s:
            if char == "|":
                isOpen = not isOpen

            if char == "*" and isOpen:
                count += 1

        return count

obj = Solution()
print(obj.countAsterisks("iampro|*grammer"))