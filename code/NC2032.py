# 给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个 元素各不相同的 数组，且由 至少 在 两个 数组中出现的所有值组成。数组中的元素可以按 任意 顺序排列。

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ret = []
        for item in nums1:
            if item in nums2:
                if item not in ret:
                    ret.append(item)

            if item in nums3:
                if item not in ret:
                    ret.append(item)

        for item in nums2:
            if item in nums3:
                if item not in ret:
                    ret.append(item)

        return ret


obj = Solution()
print(obj.twoOutOfThree([1,2,2], [4,3,3], [5]))
