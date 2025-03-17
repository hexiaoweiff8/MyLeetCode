class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        left = 0
        right = position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            cnt = 1
            cur = position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= mid:
                    cnt += 1
                    cur = position[i]
            if cnt >= m:
                left = mid
            else:
                right = mid - 1
        return left