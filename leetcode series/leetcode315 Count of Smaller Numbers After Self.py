# An actual divide-and-conquer solution, or... mergesort solution
class Solution(object):
    def countSmaller(self, nums):

        if not nums or len(nums) == 1:
            return 0

        smaller = [0] * len(nums)

        def sort(enum):  # need to pass the actual list, not just index.

            if not enum:
                return
            if len(enum) == 1:
                return enum

            half = len(enum) / 2
            left, right = sort(enum[:half]), sort(enum[half:])
            # from last to first, find the max of the remaining.
            for i in xrange(len(enum) - 1, -1, -1):
                if (not right) or (left and left[-1][-1] > right[-1][-1]):
                    # left[-1][-1] bigger than the whole right list
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
            return enum

        sort(list(enumerate(nums)))
        #print nums
        return smaller


Sol = Solution()
print Sol.countSmaller([5,6,2,1,3,4,7,8,10])
