class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        index, sLen, ret = 0, len(s), ""
        while index < sLen:
            char = s[index]
            if index in indices:
                indexIndex = indices.index(index)
                source = sources[indexIndex]
                sourceIndex = s.find(source, index)
                if sourceIndex == index:
                    ret += targets[indexIndex]
                    index += len(source) - 1
                else:
                    ret += char
            else:
                ret += char
            index += 1
        return ret


obj = Solution()
print(obj.findReplaceString(s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))
print(obj.findReplaceString(s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))
print(obj.findReplaceString(s="wreorttvosuidhrxvmvo", indices=[14, 12, 10, 5, 0, 18],
                            sources=["rxv", "dh", "ui", "ttv", "wreor", "vo"],
                            targets=["frs", "c", "ql", "qpir", "gwbeve", "n"]))
