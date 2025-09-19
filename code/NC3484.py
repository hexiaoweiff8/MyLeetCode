class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        # 修复：为每一行创建独立的列表，避免引用同一个列表对象
        self.rows = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.rows[int(cell[1:]) - 1][ord(cell[0]) - ord('A')] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.rows[int(cell[1:]) - 1][ord(cell[0]) - ord('A')] = 0

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # 解析字符串
        cells = formula[1:].split('+')
        # 如果第一个字符是字母这
        ans = 0
        for cell in cells:
            if cell[0].isalpha():
                ans += self.rows[int(cell[1:]) - 1][ord(cell[0]) - ord('A')]
            else:
                ans += int(cell)
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(3)
# print(obj.getValue("=5+7"))
# obj.setCell("A1", 10)
# print(obj.getValue("=A1+6"))
# obj.setCell("B2", 15)
# print(obj.getValue("=A1+B2"))
# obj.resetCell("A1")
# print(obj.getValue("=A1+B2"))


obj = Spreadsheet(458)
print(obj.getValue("=O126+10272"))