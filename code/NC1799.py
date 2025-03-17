class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        listLen = len(nums)
        for index in range(listLen):
            item = nums[index]
            for index2 in range(index + 1, listLen):
                item2 = nums[index2]
                pubVal = self.pub(item, item2)
                if pubVal != 1 and dict.get(pubVal, None) is None:
                    dict[pubVal] = []
                dict[pubVal].append((item, item2))
        print(dict)
        print(max(dict))
        # 计算排序分数
        while len(dict) > 0:
            pass

    # 最大公约数
    def pub(self, num1, num2):
        while num2 != 0:
            temp = num1
            num1 = num2
            num2 = temp % num2
        return num1


obj = Solution()
print(obj.maxScore([3, 4, 6, 8]))
