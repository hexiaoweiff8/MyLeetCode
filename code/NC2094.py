class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = set()
        digits.sort()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if j == i:
                    continue
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0:
                        ans.add(100 * digits[i] + 10 * digits[j] + digits[k])
        ans = list(ans)
        ans.sort()
        return ans