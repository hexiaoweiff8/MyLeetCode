class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        mCnt = l = oneCnt = 0
        ansList = []
        for i in range(len(s)):
            if s[i] == '1':
                oneCnt += 1
            while oneCnt >= k:
                if mCnt == 0 or i - l + 1 <= mCnt:
                    ansList.append(s[l:i+1])
                mCnt = min(mCnt, i - l + 1)
                if s[l] == '1':
                    oneCnt -= 1
                l += 1
        ansList.sort(key=lambda x: (len(x), x))
        return ansList[0] if len(ansList) > 0 else ''