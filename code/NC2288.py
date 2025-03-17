class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        res = sentence.split(" ")
        for i in range(len(res)):
            # 判断$开头的数字
            if res[i][0] == "$" and res[i][1:].isdigit():
                res[i] = "$" + "{:.2f}".format(float(res[i][1:]) * (100 - discount) / 100)
        return " ".join(res)


obj = Solution()
print(obj.discountPrices("there are $1 $2 and 5$ candies in the shop", 50))