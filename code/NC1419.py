class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        mp = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        indexDic = [0, 0, 0, 0, 0]
        maxWeight = 1
        for char in croakOfFrogs:
            index = mp[char]
            if indexDic and index != 0:
                if indexDic[index] == 0:
                    return -1
                indexDic[index] -= 1
                if index < 4:
                    indexDic[index + 1] += 1
            elif index == 0:
                indexDic[index + 1] += 1
            else:
                return -1

            maxWeight = max(maxWeight, sum(indexDic))
        if sum(indexDic) > 0:
            return -1
        return maxWeight


obj = Solution()
print(obj.minNumberOfFrogs("croakcroak"))
print(obj.minNumberOfFrogs("crcoakroak"))
print(obj.minNumberOfFrogs("croakcrook"))
print(obj.minNumberOfFrogs("croakcroa"))
print(obj.minNumberOfFrogs("ccrrooaakk"))
print(obj.minNumberOfFrogs("cccrrocarkooraakkoak"))
