class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for item in s:
            count = dict.get(item, 0) + 1
            if count >= 2:
                return item
            dict[item] = count