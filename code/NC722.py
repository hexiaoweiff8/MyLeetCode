class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        t, ans = [], []
        isBlock = False
        for line in source:
            i = 0
            lenLine = len(line)
            while i < lenLine:
                if isBlock:
                    if i + 1 < lenLine and line[i] == "*" and line[i + 1] == "/":
                        isBlock = False
                        i += 1
                else:
                    if i + 1 < lenLine and line[i] == "/" and line[i + 1] == "*":
                        isBlock = True
                        i += 1
                    elif i + 1 < lenLine and line[i] == "/" and line[i + 1] == "/":
                        break
                    else:
                        t.append(line[i])
                i += 1
            if not isBlock and t:
                ans.append("".join(t))
                t.clear()
        return ans
        #         plus = ""
        #         for index, char in enumerate(line):
        #             if not scopeType:
        #                 plus += char
        #             if char == "/":
        #                 if preChar == "/" and prePreChar != "*":
        #                     plus = plus[:len(plus) - 2]
        #                     plus += "\n"
        #                     break
        #                 elif preChar == "*" and prePreChar != "/":
        #                     scopeType = False
        #             elif char == "*":
        #                 if preChar == "/" and not scopeType:
        #                     scopeType = True
        #                     plus = plus[:len(plus) - 2]
        #             prePreChar = preChar
        #             preChar = char
        #             if index == len(line) - 1 and not scopeType:
        #                 plus += "\n"
        #         if plus and plus != "\n":
        #             ans += plus
        #     else:
        #         scopeEndIndex = line.find("*/")
        #         if -1 < scopeEndIndex:
        #             if line[scopeEndIndex + 2:]:
        #                 ans += line[scopeEndIndex + 2:]
        #             ans += ("\n" if plus else "")
        #             scopeType = False
        # if len(ans) > 2:
        #     return ans[:-1].split("\n")
        # else:
        #     return []


obj = Solution()
print(obj.removeComments(source=["a//*b//*c", "blank", "d/*/e*//f"]))
print(obj.removeComments(
    source=["main() {", "   func(1);", "   /** / more comments here", "   float f = 2.0", "   f += f;",
            "   cout << f; */", "}"]))
print(
    obj.removeComments(source=["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]))
print(obj.removeComments(source=["a/*comment", "line", "more_comment*/b"]))
print(obj.removeComments(
    source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
            "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
print(obj.removeComments(
    source=["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]))
print(obj.removeComments(
    source=["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))
print(obj.removeComments(
    source=["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]))
