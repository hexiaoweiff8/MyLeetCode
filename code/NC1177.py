class Solution(object):
    def canMakePaliQueries(self, s, queries):
        ret = []
        n = len(s)
        # 统计前缀和
        countList = [[0] * 26 for _ in range(n + 1)]
        for index, char in enumerate(s, 1):
            countList[index] = countList[index - 1][:]
            countList[index][ord(char) - ord("a")] += 1
        for left, right, k in queries:
            count = sum((countList[right + 1][i] - countList[left][i]) & 1 for i in range(26))
            ret.append(count // 2 <= k)
        return ret


obj = Solution()
print(obj.canMakePaliQueries(s="abcda", queries=[[0, 4, 1]]))
print(obj.canMakePaliQueries("hunu", [[0, 3, 1], [1, 1, 1]]))
