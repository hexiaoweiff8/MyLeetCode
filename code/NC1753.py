class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # 从abc中获取最大两个值减1并计分
        score = 0
        list = [a, b, c]
        list.sort()
        while True:
            if list[1] > 0 and list[2] > 0:
                list[1] -= 1
                list[2] -= 1
                score += 1
                list.sort()
            else:
                break
        return score


obj = Solution()
print(obj.maximumScore(1, 8, 8))


'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        s = a + b + c
        max_val = max(a, b, c)
        return s - max_val if s < max_val * 2 else s // 2
'''