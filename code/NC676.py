class MagicDictionary(object):

    def __init__(self):
        self.tree = {}

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            node = self.tree
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        isError = False
        node = self.tree
        stack = []
        stack.append(searchWord[0])
        searchWord = searchWord[1:]
        while stack:
            c = stack.pop()
            if c in node:
                if searchWord:
                    stack.append(searchWord[0])
                    searchWord = searchWord[1:]
                    node = node[c]
                else:
                    return True
            elif not isError:
                # 将当前数下所有节点进行搜索(跳过错误)
                for k in node:
                    stack.append(k)
                isError = True
            else:
                return False
        return True



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)