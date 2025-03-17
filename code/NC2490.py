class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        ret = True
        array = sentence.split(" ")
        for index in range(1, len(array)):
            preItem, item = array[index - 1], array[index]
            if item[0] != preItem[-1]:
                ret = False
                break
        return sentence[0] == sentence[-1] and ret


obj = Solution()
print(obj.isCircularSentence("leetcode exercises sound delightful"))
print(obj.isCircularSentence("eetcode"))
print(obj.isCircularSentence("Leetcode is cool"))
print(obj.isCircularSentence("leetcode eats soul"))