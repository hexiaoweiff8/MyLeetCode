from bisect import bisect_right


class SnapshotArray(object):

    def __init__(self, length):
        self.arr = [[] for _ in range(length)]
        self.snapId = 0

    def set(self, index, val):
        self.arr[index].append((self.snapId, val))

    def snap(self):
        ret = self.snapId
        self.snapId += 1
        return ret

    def get(self, index, snap_id):
        ret = bisect_right(self.arr[index], (snap_id + 1, -1))
        return 0 if ret == 0 else self.arr[index][ret - 1][1]



# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
print(obj.snap())
obj.set(0, 6)
print(obj.get(0, 0))