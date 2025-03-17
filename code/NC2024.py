class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        n = len(answerKey)
        def slide(c):
            left, ans, sumVal = 0, 0, 0
            for right in range(n):
                sumVal += answerKey[right] != c
                while sumVal > k:
                    print(left, answerKey[left] != c)
                    sumVal -= answerKey[left] != c
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(slide('T'), slide('F'))


obj = Solution()
# print(obj.maxConsecutiveAnswers(answerKey = "TTFF", k = 2))
print(obj.maxConsecutiveAnswers(answerKey = "FFFTTFTTFT", k = 3))