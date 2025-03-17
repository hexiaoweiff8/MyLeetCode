class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.chars = []
        self.treeMap = TreeMap()
        self.maxWordLen = 0
        for word in words:
            self.treeMap.addItem(word[::-1])
            if self.maxWordLen < len(word):
                self.maxWordLen = len(word)

    def query(self, letter=None):
        """
        :type letter: str
        :rtype: bool
        """
        if letter:
            self.chars.append(letter)
            check, isSub = self.treeMap.checkIsEnd(reversed(self.chars[-self.maxWordLen:]))
            if check:
                return True
        return False


class TreeMap(object):
    """
    字符串树字典
    """

    def __init__(self):
        self.map = {}

    def addItem(self, item):
        if item:
            map = self.map
            itemLen = len(item)
            for index in range(itemLen):
                char = item[index]
                nextMap = map.get(char, None)
                if not nextMap:
                    nextMap = {}
                    map[char] = nextMap
                if index == itemLen - 1:
                    nextMap["isEnd"] = True
                map = nextMap

    def check(self, item):
        if item:
            map = self.map
            for char in item:
                nextMap = map.get(char, None)
                if nextMap is None:
                    return False
                map = nextMap
            return True
        return False

    def checkIsEnd(self, item):
        if item:
            map = self.map
            for char in item:
                nextMap = map.get(char, None)
                if nextMap is None:
                    return False, False
                if nextMap.get("isEnd", False):
                    return True, True
                map = nextMap
            return map.get("isEnd", False), True
        return False, False


# obj = TreeMap()
# obj.addItem("aabbba")
# obj.addItem("aabbca")
# print(obj.check("aabbba"))
# print(obj.checkIsEnd("aabbc"))
# print("123abcdefg123"[0:])

data = [["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["b"], ["b"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"],
        ["b"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"],
        ["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"]]
streamChecker = StreamChecker(["abaa", "abaab", "aabbb", "bab", "ab"])
ans = [False, False, True, False, True, False, False, True, False, False, False, False, False, True, False, True, False,
       False, False, True, False, False, False, False, False, False, False, True, False, True, False, False, False,
       False, True, False, True, False, True, False]
index = 0
for item in data:
    ret = streamChecker.query(item[0])
    print(ret, ans[index], ret == ans[index])
    if ret != ans[index]:
        streamChecker.query()
    index += 1
# streamChecker = StreamChecker(["cd", "f", "kl"])
# print(streamChecker.query("a"))  # 返回 False
# print(streamChecker.query("b"))  # 返回 False
# print(streamChecker.query("c"))  # 返回n False
# print(streamChecker.query("d"))  # 返回 True ，因为 'cd' 在 words 中
# print(streamChecker.query("e"))  # 返回 False
# print(streamChecker.query("f"))  # 返回 True ，因为 'f' 在 words 中
# print(streamChecker.query("g"))  # 返回 False
# print(streamChecker.query("h"))  # 返回 False
# print(streamChecker.query("i"))  # 返回 False
# print(streamChecker.query("j"))  # 返回 False
# print(streamChecker.query("k"))  # 返回 False
# print(streamChecker.query("l"))  # 返回 True ，因为 'kl' 在 words 中
