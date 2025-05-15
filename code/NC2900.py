class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        ans = []
        n = len(words)
        for i, g in enumerate(groups):
            if i == n - 1 or g != groups[i + 1]:
                ans.append(words[i])
        return ans