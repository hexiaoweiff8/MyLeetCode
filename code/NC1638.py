class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ret = 0
        lenT = len(t)
        lenS = len(s)
        treeMap = TreeMap()
        for index in range(lenT):
            treeMap.addItem(t[index:])
        for index in range(lenS):
            for index2 in range(index + 1, lenS + 1):
                checkStr = s[index: index2]
                # 统计单个字母不相同的数量
                ret += treeMap.checkCount(checkStr)

        return ret


class TreeMap(object):
    """
    字符串树字典
    """

    def __init__(self):
        self.map = {}
        self.history = {}

    def addItem(self, item):
        if item:
            tmpMap = self.map
            itemLen = len(item)
            for index in range(itemLen):
                char = item[index]
                nextMap = tmpMap.get(char, None)
                if not nextMap:
                    nextMap = {}
                    tmpMap[char] = nextMap
                nextMap["count"] = nextMap.get("count", 0) + 1
                tmpMap = nextMap
            self.map["count"] = self.map.get("count", 0) + 1
            tmpMap["isEnd"] = True

    def checkCount(self, item):
        if item:
            if self.history.get(item, None):
                return self.history[item]
            tmpMap = self.map
            itemLen = len(item)
            count = 0
            for index in range(itemLen):
                char = item[index]
                # 处理前缀不同的字符串
                for key, node in tmpMap.items():
                    if len(key) == 1 and key != char:
                        if index + 1 < itemLen:
                            plusCount = 0
                            # 多个字符情况
                            for index2 in range(index + 1, itemLen):
                                char2 = item[index2]
                                # 遍历所有字符串
                                if char2 not in node:
                                    plusCount = 0
                                    break
                                node = node[char2]
                                if index2 + 1 == itemLen:
                                    plusCount += node.get("count", 0)
                            count += plusCount
                        else:
                            # 单个字符情况
                            count += node.get("count", 0)

                if char not in tmpMap:
                    break
                # 处理后缀不同的字符串
                tmpMap = tmpMap.get(char)
            # print(item, count)
            self.history[item] = count
            return count


obj = Solution()
print(obj.countSubstrings("aba", "baba"))
print(obj.countSubstrings("ab", "bb"))
print(obj.countSubstrings("a", "a"))
print(obj.countSubstrings("abe", "bbc"))
print(obj.countSubstrings("abe", "aba"))
print(obj.countSubstrings("abbab", "bbbbb"))
