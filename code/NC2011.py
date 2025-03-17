class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        sum = 0
        for item in operations:
            if item[0] == '-' or item[2] == '-':
                sum -= 1
            else:
                sum += 1

        return sum