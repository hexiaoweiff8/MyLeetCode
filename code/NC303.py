class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.preNumsSum = [0] * len(nums)
        self.preNumsSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.preNumsSum[i] = self.preNumsSum[i - 1] + nums[i]


    def sumRange(self, left, right):
        return self.preNumsSum[right] - self.preNumsSum[left] + self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
