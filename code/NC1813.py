class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        if sentence1 == sentence2:
            return True

        sentances1 = sentence1.split(" ")
        sentances2 = sentence2.split(" ")
        len1 = len(sentances1)
        len2 = len(sentances2)

        if len1 < len2:
            tmp = sentances1
            sentances1 = sentances2
            sentances2 = tmp
            tmp = len1
            len1 = len2
            len2 = tmp
        elif len1 == len2:
            return False

        index1 = 0
        index2 = len1 - 1
        index3 = len2 - 1
        while index1 < len2 and sentances1[index1] == sentances2[index1]:
            index1 += 1

        while index3 >= index1 and sentances1[index2] == sentances2[index3]:
            index2 -= 1
            index3 -= 1

        return index1 > index3


obj = Solution()
print(obj.areSentencesSimilar("A lot of words", "of"))
