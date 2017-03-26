
import random

class RandomizedSet(object):

    def __init__(self):

        self.array = []
        self.dic = {}

    def insert(self, val):

        if val in self.dic: return False
        self.array.append(val)
        self.dic[val] = len(self.array) - 1
        return True

    def remove(self, val):

        if val not in self.dic: return False
        index = self.dic[val]
        # the element that needs to be moved to the index of deleted element
        newval = self.array[-1]
        self.array[-1], self.array[index] = val, newval
        self.array.pop()
        # we update the index of moved element first, then delete the deleted element
        # from dic, because we need to consider the case when newval == val
        self.dic[newval] = index
        del self.dic[val]
        return True

    def getRandom(self):

        randindex = random.randint(0, len(self.array) - 1)
        return self.array[randindex]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()