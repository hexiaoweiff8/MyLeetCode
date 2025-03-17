from collections import Counter


class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(1, n):
            if n % i == 0:
                dic = Counter(s[:i])
                # 计算
                isSame = True
                for j in range(i, n, i):
                    dic2 = Counter(s[j:j + i])
                    # 判断练个dic中的数量是否相同
                    if dic != dic2:
                        isSame = False
                        break
                if isSame:
                    return i
        return n


obj = Solution()
print(obj.minAnagramLength("aabb"))