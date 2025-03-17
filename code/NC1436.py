class Solution(object):
    def destCity(self, paths):
        target = {}
        for i in paths:
            target[i[0]] = i[1]
        for i in paths:
            if i[1] not in target:
                return i[1]

        