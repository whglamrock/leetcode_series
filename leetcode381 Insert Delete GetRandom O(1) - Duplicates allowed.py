from collections import defaultdict
from random import randint

# 1) The reason we need to use set instead of list to store the indexes is because when we do the swapping, we won't be able to
# keep the indexes of the number to be swapped "in" sorted with O(1) time if we insert "indexOfRemoved" into a list
# 2) Remember using Python set.pop() operation, which is amortized O(1) time
class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.numToIndexes = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val not in self.numToIndexes:
            self.numToIndexes[val].add(len(self.nums))
            self.nums.append(val)
            return True
        else:
            self.numToIndexes[val].add(len(self.nums))
            self.nums.append(val)
            return False

    def remove(self, val: int) -> bool:
        if val not in self.numToIndexes:
            return False

        if self.nums[-1] == val:
            self.numToIndexes[val].discard(len(self.nums) - 1)
            if not self.numToIndexes[val]:
                del self.numToIndexes[val]
            self.nums.pop()
            return True
        else:
            indexOfRemoved = self.numToIndexes[val].pop()
            if not self.numToIndexes[val]:
                del self.numToIndexes[val]

            indexToDiscard = len(self.nums) - 1
            numToSwap = self.nums[-1]
            self.numToIndexes[numToSwap].discard(indexToDiscard)
            self.numToIndexes[numToSwap].add(indexOfRemoved)
            self.nums[indexOfRemoved] = numToSwap
            self.nums.pop()
            return True

    def getRandom(self) -> int:
        randomIndex = randint(0, len(self.nums) - 1)
        return self.nums[randomIndex]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
