from collections import Counter


class Solution(object):
    def takeCharacters(self, s, k):
        counter = Counter(s)
        if any(counter[c] < k for c in "abc"):
            return -1
        ans = left = 0
        for right, c in enumerate(s):
            counter[c] -= 1
            while counter[c] < k:
                counter[s[left]] += 1
                left += 1
            ans = max(ans, right - left + 1)

        return len(s) - ans


obj = Solution()
print(obj.takeCharacters("babbaacbba", 4))