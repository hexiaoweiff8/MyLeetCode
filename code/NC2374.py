from collections import Counter

class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        suitCount = Counter(suits)
        if suitCount[max(suitCount, key=suitCount.get)] >= 5:
            return "Flush"

        rankCount = Counter(ranks)
        if rankCount[max(rankCount, key=rankCount.get)] >= 3:
            return "Three of a Kind"
        if rankCount[max(rankCount, key=rankCount.get)] == 2:
            return "Pair"
        return "High Card"


ranks = [10,10,2,12,9]
suits = ["a","b","c","a","d"]
obj = Solution()
print(obj.bestHand(ranks, suits))
