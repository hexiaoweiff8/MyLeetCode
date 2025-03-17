class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        n = len(palindrome)
        for i in range(n):
            if palindrome[i] != 'a':
                char = 'a'
                if palindrome[n - i - 1] == char:
                    char = 'b'
                return palindrome[:i] + char + palindrome[i + 1:]

