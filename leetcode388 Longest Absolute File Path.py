
# idea from Stefan: https://discuss.leetcode.com/topic/55097/simple-python-solution
# rememeber the use of lstrip (left strip the chars from a string)!

class Solution(object):
    def lengthLongestPath(self, input):

        input = input.splitlines()  # split lines: split the string by '\n'
        path = {0: 0}
        maxlen = 0
        for line in input:
            name = line.lstrip('\t')    # P.S.: '\t' only counts for one char!!, try print len(line) - len(name)
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, path[depth] + len(name))
                # no need to +1 cuz there won't be any more suffixes to add.
            else:
                path[depth + 1] = path[depth] + len(name) + 1
                # +1 to count the '/' that would be added in the middle of two depths.

        return maxlen