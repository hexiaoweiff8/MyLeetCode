class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        dic = {}
        for index in range(len(names)):
            sourceName = name = names[index]
            sourceCount = dic.get(sourceName, 0)
            if sourceCount > 0:
                dic[sourceName] = sourceCount + 1
                while sourceName + "(" + str(sourceCount) + ")" in dic:
                    sourceCount += 1
                names[index] = sourceName + "(" + str(sourceCount) + ")"
                dic[names[index]] = dic.get(names[index], 0) + 1
            else:
                num = 0
                if name.endswith(")"):
                    num = int(name[-2: -1])
                    name = name[:-3]
                count = dic.get(name, 0)
                if count > 0:
                    if count == num:
                        dic[name] += 1
                    dic[names[index]] = dic.get(names[index], 0) + 1

                dic[sourceName] = 1

        return names


obj = Solution()
# print(obj.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
# print(obj.getFolderNames(["wano", "wano", "wano", "wano"]))
# print(obj.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
# print(obj.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]))
# print(obj.getFolderNames(["kingston(0)", "kingston", "kingston"]))
# print(obj.getFolderNames(["d(1)", "z(1)(4)", "z(1)", "z(2)", "d"]))
# print(obj.getFolderNames(["m", "m(3)", "m"]))
# print(obj.getFolderNames(["p", "p(2)"]))
print(obj.getFolderNames(["b(1)", "b", "b"]))
