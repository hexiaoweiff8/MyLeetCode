from collections import Counter


class FrequencyTracker(object):

    def __init__(self):
        self.countDic = Counter()
        self.numberDic = Counter()

    def add(self, number):
        self.countDic[self.numberDic[number]] -= 1
        self.numberDic[number] += 1
        self.countDic[self.numberDic[number]] += 1

    def deleteOne(self, number):
        self.countDic[self.numberDic[number]] -= 1
        self.numberDic[number] = max(self.numberDic[number] - 1, 0)
        self.countDic[self.numberDic[number]] += 1

    def hasFrequency(self, frequency):
        return self.countDic[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:

op = ["deleteOne", "deleteOne", "add", "hasFrequency", "hasFrequency", "hasFrequency"]
params = [[2], [1], [1], [1], [1], [1]]
obj = FrequencyTracker()
ans = [True, True, True]
j = 0
for i in range(len(op)):
    if op[i] == "add":
        obj.add(params[i][0])
    if op[i] == "deleteOne":
        print("delete", params[i][0])
        obj.deleteOne(params[i][0])
    if op[i] == "hasFrequency":
        ret = obj.hasFrequency(params[i][0])
        print(ret, "isRight", ret == ans[j])
        j += 1
