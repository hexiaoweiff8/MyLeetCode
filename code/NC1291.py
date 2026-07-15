class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        s = "123456789"
        for length in range(2, 10):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if num > high:
                    return ans
                if num >= low:
                    ans.append(num)
        return ans
