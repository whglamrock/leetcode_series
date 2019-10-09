
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.size = 0
        self.numSet = set()
        self.valToIndex = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.numSet:
            self.numSet.add(val)
            # add to tail first
            self.nums.append(val)
            # if the last few numbers are invalid, swap the new value to the end of the valid prefix
            self.swap(self.size, -1)
            self.valToIndex[val] = self.size
            self.size += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.numSet:
            # remove from numSet
            self.numSet.discard(val)
            # remove from valToIndex
            index = self.valToIndex[val]
            del self.valToIndex[val]
            # remove from nums & update the index of the swapped value
            valToSwap = self.nums[self.size - 1]
            self.swap(index, self.size - 1)
            self.valToIndex[valToSwap] = index
            # don't forget to decrease the size
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomIndex = random.randrange(0, self.size)
        return self.nums[randomIndex]

    def swap(self, i, j):
        tmp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = tmp




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()