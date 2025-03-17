from collections import Counter


class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ret = ""
        countDic = Counter(s)
        if countDic["1"] == 1:
            for i in range(len(s) - 1):
                ret += "0"
        else:
            for i in range(countDic["1"] - 1):
                ret += "1"
            for i in range(countDic["0"]):
                ret += "0"
        return ret + "1"

    def maximumOddBinaryNumber2(self, s):
        cnt = s.count("1")
        return "1" * (cnt - 1) + "0" * (len(s) - cnt) + "1"