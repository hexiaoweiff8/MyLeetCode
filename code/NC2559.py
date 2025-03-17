class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        yuanSet = set("aeiou")
        yuanList = []
        ret = []

        def search(x):
            l, r = 0, len(yuanList)
            while l < r:
                mid = (l + r) // 2
                if yuanList[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l
        for index in range(len(words)):
            word = words[index]
            if word[0] in yuanSet and word[-1] in yuanSet:
                yuanList.append(index)
        for query in queries:
            ret.append(search(query[1] + 1) - search(query[0]))

        return ret


obj = Solution()
print(obj.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
print(obj.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))