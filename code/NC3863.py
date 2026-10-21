class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 转为数组
        sArr = list(s)
        # 判断是否已经是顺序的
        sArr.sort()
        mx = max(sArr)
        mn = min(sArr)
        if s == ''.join(sArr):
            return 0
        elif len(s) == 2:
            return -1
        # 判断第一个是否为最小或者最后一个是否为最大的字母
        if s[-1] == mx or mn == s[0]:
            return 1
        if any(ch == mn or ch == mx for ch in s[1: -1]):
            return 2

        return 3


obj = Solution()
print(obj.minOperations("gf"))