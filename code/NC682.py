class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        ret = 0
        for op in operations:
            if op == 'C':
                ret -= stack.pop()
            else:
                if op == '+':
                    stack.append(stack[-1] + stack[-2])
                elif op == 'D':
                    stack.append(stack[-1] * 2)
                else:
                    stack.append(int(op))
                ret += stack[-1]

        return ret


obj = Solution()
print(obj.calPoints(["5","2","C","D","+"]))