class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        mapData = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in mapData:
                stack.append(char)
            elif stack:
                popChar = stack.pop()
                if mapData[popChar] != char:
                    return False
            else:
                return False
        return len(stack) == 0


obj = Solution()
print(obj.isValid("()[]{}"))
print(obj.isValid("()"))
print(obj.isValid("(]{}"))
print(obj.isValid("(("))
print(obj.isValid("){"))