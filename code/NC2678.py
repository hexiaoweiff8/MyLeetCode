class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        ret = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ret += 1
        return ret