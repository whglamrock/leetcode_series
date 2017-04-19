
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

# important idea: stack

class NestedIterator(object):

    def __init__(self, nestedList):

        self.lst = []
        while nestedList:
            item = nestedList.pop()
            if item.isInteger():
                self.lst.append(item.getInteger())
            else:
                for subitem in item.getList():
                    nestedList.append(subitem)

    def next(self):

        # I guess we don't need to check if it hasNext()? because it should be
        #   already checked before this function being called
        return self.lst.pop()

    def hasNext(self):

        return len(self.lst) != 0



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



'''
# recursive solution:

class NestedIterator(object):

    def __init__(self, nestedList):

        self.pool = []
        def flatten(nestedList):
            for item in nestedList:
                if item.isInteger():
                    self.pool.append(item.getInteger())
                else:
                    newnestedList = item.getList()
                    flatten(newnestedList)
        flatten(nestedList)
        self.pool.reverse()

    def next(self):

        if self.hasNext():
            return self.pool.pop()

    def hasNext(self):

        return len(self.pool) != 0
'''