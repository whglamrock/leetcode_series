'''
Google OA question.
Core idea within the last for loop
'''
class Solution(object):
    def getModifiedArray(self, length, updates):

        res = [0 for i in xrange(length)]
        for update in updates:
            start, end, inc = update
            res[start] += inc   # only update the start element

            if end + 1 <= length - 1:   # try the whole solution with updates == [[1,  3,  2]]
                res[end+1] -= inc  # in this try, we can see there is no need to update all res[end+1:]

        sum = 0
        for i in range(length):
            sum += res[i]   # the core idea: at last, every element is the sum of all previous
            res[i] = sum    # elements in the status after the first loop.
        return res


length = 5
updates = [
           [1,  3,  2],
           [2,  4,  3],
           [0,  2, -2]
           ]
Sol = Solution()
print Sol.getModifiedArray(length, updates)