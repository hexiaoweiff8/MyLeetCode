class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        """
        opStack = []
        numStack = []
        preChar = ","
        for char in expression:
            if char == "{":
                if preChar != "," and preChar != "{":
                    opStack.append("*")
                opStack.append(char)
            elif char == "}":
                # 处理前置乘法
                while opStack[-1] != "{":
                    op = opStack.pop()
                    s2 = numStack.pop()
                    s1 = numStack.pop()
                    if op == "*":
                        numStack.append({e1 + e2 for e1 in s1 for e2 in s2})
                    elif op == "+":
                        numStack.append(s1.union(s2))
                opStack.pop()
            elif char == ",":
                while opStack and opStack[-1] == "*":
                    opStack.pop()
                    s2 = numStack.pop()
                    s1 = numStack.pop()
                    numStack.append({e1 + e2 for e1 in s1 for e2 in s2})
                opStack.append("+")
            else:
                numStack.append({char})
                if preChar != "," and preChar != "{":
                    opStack.append("*")
            preChar = char

        while opStack:
            op = opStack.pop()
            s2 = numStack.pop()
            s1 = numStack.pop()
            if op == "*":
                numStack.append({e1 + e2 for e1 in s1 for e2 in s2})
            elif op == "+":
                numStack.append(s1 + s2)

        return sorted(numStack.pop())


obj = Solution()
print(obj.braceExpansionII("a{c}b"))
print(obj.braceExpansionII("a{c,{d,e}}"))
print(obj.braceExpansionII("{a,b}{c,{d,e}}"))
print(obj.braceExpansionII("{a{b,c},{ab,z}}"))
print(obj.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
print(obj.braceExpansionII("{a,b}c{d,e}f"))
print(obj.braceExpansionII("abcd"))
print(obj.braceExpansionII("{p,q,r}{s,t}a{x,z}z"))
print(obj.braceExpansionII("n{g,{u,o}}{a,{x,ia,o},w}"))
print(obj.braceExpansionII("{a{x,ia,o}w,{n,{g,{u,o}},{a,{x,ia,o},w}},er}"))
print(obj.braceExpansionII("{a,{a,{x,ia,o},w}er{n,{g,{u,o}},{a,{x,ia,o},w}},er}"))
