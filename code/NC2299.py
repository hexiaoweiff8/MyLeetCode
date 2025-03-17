class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        signDict = {
            '!': True,
            '@': True,
            '#': True,
            '$': True,
            '%': True,
            '^': True,
            '&': True,
            '*': True,
            '(': True,
            ')': True,
            '-': True,
            '+': True
        }
        isUpper = False
        isLower = False
        isDigit = False
        isSign = False
        isCChar = False
        preChar = ''
        if len(password) < 8:
            return False

        for char in password:
            if char.isdigit():
                isDigit = True
            elif char.islower():
                isLower = True
            elif char.isupper():
                isUpper = True
            elif char in signDict:
                isSign = True
            if preChar == char:
                isCChar = True
            preChar = char

        return isUpper and isLower and isDigit and isSign and not isCChar

obj = Solution()
print(obj.strongPasswordCheckerII("11A!A!Aa"))
