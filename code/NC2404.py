class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        maxCount = 0
        for num in nums:
            if num % 2 == 0:
                dic[num] = dic.get(num, 0) + 1
                if dic[num] > maxCount:
                    maxCount = dic[num]

        minNum = 999999
        for key, val in dic.items():
            if val == maxCount and minNum > key:
                minNum = key

        return minNum if minNum != 999999 else -1


obj = Solution()
print(obj.mostFrequentEven([0,1,2,2,4,4,1]))
print(obj.mostFrequentEven([4,4,4,9,2,4]))
print(obj.mostFrequentEven([29,47,21,41,13,37,25,7]))
