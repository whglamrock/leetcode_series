from random import randint

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.valToIndex = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val not in self.valToIndex:
            self.valToIndex[val] = self.size
            if self.size == len(self.nums):
                self.nums.append(val)
            else:
                self.nums[self.size] = val
            self.size += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False
        else:
            valToSwap = self.nums[self.size - 1]
            index = self.valToIndex[val]
            self.nums[index] = valToSwap
            self.valToIndex[valToSwap] = index
            # delete it at last because in some edge cases valToSwap == val
            del self.valToIndex[val]
            self.size -= 1
            return True

    def getRandom(self) -> int:
        randomInt = randint(0, self.size - 1)
        return self.nums[randomInt]


randomSet = RandomizedSet()
print(randomSet.insert(1))
print(randomSet.remove(2))
print(randomSet.insert(2))
print(randomSet.getRandom())
print(randomSet.remove(1))
print(randomSet.insert(2))
print(randomSet.getRandom())
