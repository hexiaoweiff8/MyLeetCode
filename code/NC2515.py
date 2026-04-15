class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        index = startIndex
        end = n = len(words)
        minVal = 99999999
        step = 0
        while end >= 0:
            if words[index] == target:
                minVal = min(minVal, step, n - step)
            end -= 1
            step += 1
            index = (index + 1) % n
        return -1 if minVal == 99999999 else minVal


obj = Solution()
print(obj.closestTarget(["hello","i","am","leetcode","hello"], "hello", 1))
