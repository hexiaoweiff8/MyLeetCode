class Solution(object):
    def clearDigits(self, s):
        sList = list(s)
        ret = []
        for i in range(len(sList)):
            if sList[i].isdigit():
                ret.pop()
            else:
                ret.append(sList[i])
        return "".join(ret)
