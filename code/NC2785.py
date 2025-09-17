class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = [c for c in s if c in 'aeiouAEIOU']

        lst.sort()
        return ''.join(c if c not in 'aeiouAEIOU' else lst.pop(0) for c in s)