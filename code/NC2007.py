from collections import Counter


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 == 1:
            return []
        sets = Counter()
        changed.sort()
        res = []
        for num in changed:
            if num in sets:
                sets[num] -= 1
                if sets[num] == 0:
                    del sets[num]
            else:
                sets[num * 2] += 1
                res.append(num)
        return [] if sets else res


obj = Solution()
print(obj.findOriginalArray([1, 3, 4, 2, 6, 8]))
print(obj.findOriginalArray([6, 3, 0, 1]))
print(obj.findOriginalArray([1]))
print(obj.findOriginalArray([0,0,0,0]))
