class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        keyDic = {}
        index = 0
        charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for keyChar in key:
            if not keyDic.get(keyChar, None) and keyChar != ' ':
                keyDic[keyChar] = charList[index]
                index += 1

        ret = ''
        for msgChar in message:
            if msgChar == ' ':
                ret += msgChar
            else:
                ret += keyDic[msgChar]

        return ret

obj = Solution()
print(obj.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
