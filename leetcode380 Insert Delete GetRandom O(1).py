from random import randint

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.numToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.numToIndex:
            return False
        self.numToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numToIndex:
            return False
        indexOfVal = self.numToIndex[val]
        lastNum = self.nums[-1]
        self.nums[indexOfVal] = lastNum
        self.nums.pop()
        self.numToIndex[lastNum] = indexOfVal
        # delete this at last because the val could be the last number
        del self.numToIndex[val]

        return True

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums) - 1)]


randomSet = RandomizedSet()
print(randomSet.insert(1))
print(randomSet.remove(2))
print(randomSet.insert(2))
print(randomSet.getRandom())
print(randomSet.remove(1))
print(randomSet.insert(2))
print(randomSet.getRandom())
