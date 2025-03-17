class TextEditor(object):

    def __init__(self):
        self.chars = []
        self.cursor = 0

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        self.chars[self.cursor:self.cursor] = list(text)
        self.cursor += len(text)

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        start = max(0, self.cursor - k)
        count = min(self.cursor - start, k)
        del self.chars[start:self.cursor]
        self.cursor = start
        return count

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        self.cursor = max(0, self.cursor - k)
        return ''.join(self.chars[max(0, self.cursor - 10):self.cursor])

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        self.cursor = min(len(self.chars), self.cursor + k)
        return ''.join(self.chars[max(0, self.cursor - 10):self.cursor])



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)