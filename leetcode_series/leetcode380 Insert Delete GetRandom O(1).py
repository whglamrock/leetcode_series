
import random

class RandomizedSet(object):

    def __init__(self):

        self.values = []
        self.valuetoindex = {}

    def insert(self, val):

        if val in self.valuetoindex:
            return False
        self.values.append(val)
        self.valuetoindex[val] = len(self.values) - 1
        return True

    def remove(self, val):

        if val not in self.valuetoindex:
            return False

        # get the index of the val that needs to be deleted
        oldindex = self.valuetoindex[val]
        # get the last value that's been added to the value list
        thevaluetoswap = self.values[-1]
        # swap the above two, so the val -- the value to delete is swapped to the last element
        self.values[oldindex], self.values[-1] = thevaluetoswap, val
        # delete the val from the value list and map
        self.values.pop()
        del self.valuetoindex[val]
        # point the last value that's been recently added to value list to the index of the deleted val
        #   but be aware of the case when val == the value to swap
        if val != thevaluetoswap:
            self.valuetoindex[thevaluetoswap] = oldindex

        return True

    def getRandom(self):

        if not self.values:
            return -1

        # randint(i, j) can generate an integer in [i, j] both inclusive
        # randrange corresponds to [i, j), left inclusive right exclusive
        randindex = random.randint(0, len(self.values) - 1)
        return self.values[randindex]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()