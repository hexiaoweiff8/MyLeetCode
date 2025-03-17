class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # 动态规划
        lenBooks = len(books)
        dp = [1000000] * (lenBooks + 1)
        dp[0] = 0
        for index, book in enumerate(books):
            curW = 0
            maxH = 0
            j = index
            while j >= 0:
                curW += books[j][0]
                if curW > shelfWidth:
                    break
                maxH = max(maxH, books[j][1])
                dp[index + 1] = min(dp[index + 1], dp[j] + maxH)
                j -= 1
        return dp[lenBooks]


obj = Solution()
print(obj.minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4))
