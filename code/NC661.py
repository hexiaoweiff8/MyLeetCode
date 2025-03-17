class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 0
                s = 0
                for x in range(max(0, i - 1), min(len(img), i + 2)):
                    for y in range(max(0, j - 1), min(len(img[0]), j + 2)):
                        s += img[x][y]
                        count += 1
                ret[i][j] = s // count
        return ret


obj = Solution()
print(obj.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
