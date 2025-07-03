class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        st = ["a"]
        while len(st) < k:
            lenV = len(st)
            for i in range(lenV):
                # 字符变为下一个字符
                st.append(chr(ord(st[i]) + 1) if st[i] != "z" else "a")

        return st[k - 1]
