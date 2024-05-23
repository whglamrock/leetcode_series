from collections import defaultdict

class SnapshotArray:
    def __init__(self, length: int):
        self.snapId = 0
        self.indexToSnapIdToVal = defaultdict(dict)
        self.indexToSnapIds = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.indexToSnapIdToVal[index][self.snapId] = val
        self.indexToSnapIds[index].append(self.snapId)

    def snap(self) -> int:
        ans = self.snapId
        self.snapId += 1
        return ans

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.indexToSnapIdToVal:
            return 0
        if snap_id >= self.snapId:
            return 0

        maxSnapIdEqualOrSmaller = self.findMaxSnapIdEqualOrLessThan(snap_id, index)
        if maxSnapIdEqualOrSmaller == -1:
            return 0

        return self.indexToSnapIdToVal[index][maxSnapIdEqualOrSmaller]

    def findMaxSnapIdEqualOrLessThan(self, target: int, index: int) -> int:
        snapIds = self.indexToSnapIds[index]
        l, r = 0, len(snapIds) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if snapIds[m] <= target:
                    return snapIds[m]
                return -1
            if snapIds[m] <= target:
                l = m
            else:
                r = m - 1

        return -1


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
