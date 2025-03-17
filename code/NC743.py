class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dic = {}
        ret = 0
        for u, v, w in times:
            lst = dic.get(u, [])
            lst.append((v, w))
            dic[u] = lst
        stack = [(k, 0)]
        while stack:
            u, w = stack.pop()
            if u not in dic:
                continue
            maxW = 0
            for v, w2 in dic[u]:
                if v not in dic:
                    continue
                stack.append((v, w + w2))
                maxW = max(maxW, w + w2)
            del dic[u]
            ret += maxW
        if len(dic) == 0:
            return ret + 1
        return -1



obj = Solution()
print(obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))