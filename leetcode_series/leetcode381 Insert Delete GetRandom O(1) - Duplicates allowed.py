
# the idea is to always swapping the value to delete with the last element and delete the last element
# data structure used: array + hashmap

import random
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):

        self.vals = []
        self.dic = defaultdict(set)


    def insert(self, val):

        self.vals.append(val)
        self.dic[val].add(len(self.vals) - 1)
        return len(self.dic[val]) == 1


    def remove(self, val):

        if not self.dic[val]:
            return False

        # getin is a value
        getin = self.vals[-1]
        # getout is an index
        getout = self.dic[val].pop()
        self.vals[getout] = getin

        # means originally, the self.array contains only one element
        #   i.e., getin == val and len(self.array) == 1
        if not self.dic[getin]:
            del self.dic[getin]
        else:
            # the order of two following steps can't be switched
            #   e.g., when getout == len(self.vals) - 1 <=> getin == val
            self.dic[getin].add(getout)
            self.dic[getin].discard(len(self.vals) - 1)

        # it needs to be after the above getin check
        #    because we need to get rid of the old 'len(self.vals) - 1'
        self.vals.pop()
        return True


    def getRandom(self):

        return random.choice(self.vals)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()