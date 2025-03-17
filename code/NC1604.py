from sortedcontainers import SortedList


class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        lenKey = len(keyName)
        nameTimeListDic = {}
        ret = []
        for index in range(lenKey):
            name = keyName[index]
            time = keyTime[index]
            timeList = nameTimeListDic.get(name, SortedList())
            timeList.add(self.formatTime(time))
            nameTimeListDic[name] = timeList
            if len(timeList) >= 3 and name not in ret and self.checkCount(timeList):
                ret.append(name)

        ret.sort()
        return ret

    def checkCount(self, timeList):
        """
        检测count
        :param timeList:
        :return:
        """
        listLen = len(timeList)
        timeList.sort()
        index1 = 0
        index2 = 0
        while index1 < listLen and index2 < listLen:
            subVal = timeList[index2] - timeList[index1]
            if 0 <= subVal <= 60:
                if index2 - index1 + 1 >= 3:
                    return True
                index2 += 1
            else:
                index1 += 1
        return False

    def formatTime(self, time):
        """
        格式化时间
        :param time:
        :return:
        """
        timeArrays = time.split(":")
        hour = timeArrays[0]
        return int(timeArrays[0]) * 60 + int(timeArrays[1])


obj = Solution()
print(obj.alertNames(["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"],
                     ["23:20", "11:09", "23:30", "23:02", "15:28", "22:57", "23:40", "03:43", "21:55", "20:38",
                      "00:19"]))
