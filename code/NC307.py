class NumArray(object):

# 分区
"""
    def __init__(self, nums):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.sums = sums
        self.size = size
        self.nums = nums

    def update(self, index, val):
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        b1, b2 = left // self.size, right // self.size
        if b1 == b2:
            return sum(self.nums[left:right + 1])
        else:
            return sum(self.nums[left:(b1 + 1) * self.size]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * self.size:right + 1])
"""
# 线段树
'''
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.seg = [0] * (4 * len(nums))
        self.build(0, 0, len(nums) - 1)

    def build(self, nums, node, s, e):
        if s == e:
            self.seg[node] = self.nums[s]
        else:
            mid = s + (e - s) // 2
            self.build(nums, 2 * node + 1, s, mid)
            self.build(nums, 2 * node + 2, mid + 1, e)
            self.seg[node] = self.seg[2 * node + 1] + self.seg[2 * node + 2]

    def change(self, index, val, node, s, e):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, 2 * node + 1, s, m)
        else:
            self.change(index, val, 2 * node + 2, m + 1, e)
        self.seg[node] = self.seg[2 * node + 1] + self.seg[2 * node + 2]

    def range(self, left, right, node, s, e):
        if left == s and e == right:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, 2 * node + 1, s, m)
        elif left > m:
            return self.range(left, right, 2 * node + 2, m + 1, e)
        return self.range(left, m, 2 * node + 1, s, m) + self.range(m + 1, right, 2 * node + 2, m + 1, e)

    def update(self, index, val):
        self.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left, right):
        return self.range(left, right, 0, 0, self.n - 1)
'''
# 树状数组
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i, nums[i])

    def add(self, index, val):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)