class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans = 0
        preCnt = 0
        for row in bank:
            cnt = row.count('1')
            if cnt > 0:
                if preCnt:
                    ans += preCnt * cnt
                preCnt = cnt
        return ans