class Trie(object):

    def __init__(self):
        self.dic = {}

    def insert(self, word):
        node = self.dic
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True

    def search(self, word):
        node = self.dic
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix):
        node = self.dic
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)