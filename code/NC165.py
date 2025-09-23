class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        while version1 and version2:
            a, b = version1.pop(0), version2.pop(0)
            if a > b:
                return 1
            elif a < b:
                return -1

        if version1:
            # 判断是否都为0
            if all(i == 0 for i in version1):
                return 0
            return 1

        if version2:
            # 判断是否都为0
            if all(i == 0 for i in version2):
                return 0
            return -1
        return 0


