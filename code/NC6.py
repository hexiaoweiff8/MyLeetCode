class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    rows[j] += s[i]
                    i += 1
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    rows[j] += s[i]
                    i += 1
        return ''.join(rows)