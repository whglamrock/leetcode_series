
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Creating a list to store the value in iterator would be time/space consuming.

class PeekingIterator(object):
    def __init__(self, iterator):

        self.iterator = iterator
        self.peeknum = None
        if self.iterator.hasNext():
            self.peeknum = self.iterator.next()
        self.nextnum = None


    def peek(self):

        return self.peeknum


    def next(self):

        self.nextnum = self.peeknum
        if self.iterator.hasNext():
            self.peeknum = self.iterator.next()
        return self.nextnum


    def hasNext(self):

        return self.nextnum != self.peeknum



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].