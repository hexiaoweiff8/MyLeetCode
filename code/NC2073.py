class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        ans = index = 0
        while tickets[k] > 0:
            if tickets[index] > 0:
                tickets[index] -= 1
                ans += 1
            index = (index + 1) % len(tickets)
        return ans
