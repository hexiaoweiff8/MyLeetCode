class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        listStart, listTarget = [], []
        for index, char in enumerate(start):
            if char != "_":
                listStart.append((char, index))
        for index, char in enumerate(target):
            if char != "_":
                listTarget.append((char, index))
        if len(listStart) != len(listTarget):
            return False
        for index in range(len(listStart)):
            if listStart[index][0] != listTarget[index][0]:
                return False
            if listStart[index][0] == "R" and listStart[index][1] > listTarget[index][1]:
                return False
            if listStart[index][0] == "L" and listStart[index][1] < listTarget[index][1]:
                return False
        return True


obj = Solution()
print(obj.canChange(start="_L__R__R_", target="L______RR"))
print(obj.canChange(start="R_L_", target="__LR"))
print(obj.canChange(start="_R", target="R_"))
print(obj.canChange(start =
                    "_L__R__R_L",
target =
"L______RR_"))
