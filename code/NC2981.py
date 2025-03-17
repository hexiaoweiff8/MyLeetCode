class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = [[0] * 3 for _ in range(26)]
        i = 0
        n = len(s)
        baseIndex = ord('a')
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            index = ord(s[i]) - baseIndex
            length = j - i
            dic[index].append(length)
            dic[index].sort(reverse=True)
            dic[index].pop()
            i = j
        res = 0
        for item in dic:
            res = max(res, item[0] - 2, min(item[0] - 1, item[1]), item[2])
        return res if res != 0 else - 1





obj = Solution()
# print(obj.maximumLength("aaaa"))
# print(obj.maximumLength("abcdef"))
print(obj.maximumLength("abcaba"))