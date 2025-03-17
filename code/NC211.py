class WordDictionary(object):

    def __init__(self):
        self.dic = {}

    def addWord(self, word):
        node = self.dic
        for c in word:
            node[c] = {}
            node = node[c]
        node['#'] = True

    def search(self, word):
        return self.match(word, 0, self.dic)

    def match(self, word, index, node):
        if node is None:
            return False
        if index == len(word):
            return '#' in node
        c = word[index]
        if c == '.':
            for k in node:
                if self.match(word, index + 1, node[k]):
                    return True
        else:
            return node is not None and self.match(word, index + 1, node[c])
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
