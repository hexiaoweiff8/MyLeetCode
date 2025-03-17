class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for item in words:
            if item.startswith(pref):
                count += 1

        return count


obj = Solution()
print(obj.prefixCount(["pay","attention","practice","attend"], "at"))
