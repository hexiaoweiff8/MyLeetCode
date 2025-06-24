class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        def isPalindrome(num):
            return str(num) == str(num)[::-1]

        def isPalindromeList(numList):
            return numList == numList[::-1]

        ans = 1
        index = 2
        count = 1
        while count < n:
            tmpIndex = index
            numList = []
            while tmpIndex > 0:
                numList.append(tmpIndex % k)
                tmpIndex //= k
            # 判断index 是否为回文
            if not isPalindrome(index):
                index += 1
                continue
            # 校验numList是否为回文
            if isPalindromeList(numList):
                ans += index
                count += 1
            index += 1

        return ans


obj = Solution()
print(obj.kMirror(2, 5))