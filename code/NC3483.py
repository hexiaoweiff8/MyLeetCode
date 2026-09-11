class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        set_ = set()
        n = len(digits)
        for i, a in enumerate(digits):
            if a % 2:
                continue
            for j , b in enumerate(digits):
                if i == j:
                    continue
                for k, c in enumerate(digits):
                    if c == 0 or i == k or k == j:
                        continue
                    set_.add(c * 100 + b * 10 + a)
        return len(set_)