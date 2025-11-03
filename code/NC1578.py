class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        sameList = []
        pre = colors[0]
        ans = 0
        sameList.append(neededTime[0])
        for i in range(1, len(colors)):
            if colors[i] == pre:
                sameList.append(neededTime[i])
            else:
                if len(sameList) > 1:
                    ans += sum(sameList) - max(sameList)
                pre = colors[i]
                sameList = [neededTime[i]]

        if len(sameList) > 1:
            ans += sum(sameList) - max(sameList)
        return ans


obj = Solution()
print(obj.minCost("abaac", [1,2,3,4,5]))
