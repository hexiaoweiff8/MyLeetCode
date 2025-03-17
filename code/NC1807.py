class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        lenS = len(s)
        isLeft = False
        word = ''
        ret = ''
        dict = {}

        # 预处理
        for item in knowledge:
            dict[item[0]] = item[1]

        # 遍历字符串
        for index in range(lenS):
            char = s[index]
            if char == '(':
                isLeft = True
            elif char == ')':
                isLeft = False
                ret += dict.get(word, '?')
                word = ''
            else:
                if isLeft:
                    word += char
                else:
                    ret += char
        return ret

obj = Solution()
print(obj.evaluate("hi(name)"
                   , [["a","b"]]))
