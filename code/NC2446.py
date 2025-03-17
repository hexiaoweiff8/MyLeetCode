class Solution:
    def haveConflict(self, event1, event2) -> bool:
        scope11 = int(event1[0][0: 2]) * 60 + int(event1[0][3:])
        scope12 = int(event1[1][0: 2]) * 60 + int(event1[1][3:])
        scope21 = int(event2[0][0: 2]) * 60 + int(event2[0][3:])
        scope22 = int(event2[1][0: 2]) * 60 + int(event2[1][3:])
        return scope11 <= scope21 <= scope12 \
               or scope11 <= scope22 <= scope12 \
               or scope21 <= scope11 <= scope22 \
               or scope21 <= scope12 <= scope22
        return not(event1[1] < event2[0] or event2[1] < event1[0])

obj = Solution()
print(obj.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))
print(obj.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))
print(obj.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]))
print(obj.haveConflict(["15:19","17:56"],
                       ["14:11","20:02"]))
