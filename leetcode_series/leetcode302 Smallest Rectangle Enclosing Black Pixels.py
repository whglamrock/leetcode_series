
# pay attention to the detail of binary search: the boundary (len(image) not len(image) - 1),
# the while condition(in this case, 'i < j' is more convenient).
# the great use of "any" built-in function.
# Most importantly, remember in this case searching if the '1' exists in a column takes
# O(N) time, because for case like '000100101' we don't know which way to go with binary
# search, we can't only scan the element one by one

class Solution(object):
    def minArea(self, image, x, y):

        top = self.searchrows(image, 0, x, True)
        # looks for the first row that contains '1'
        bottom = self.searchrows(image, x + 1, len(image), False)
        # looks for the first row that doesn't contain '1'
        left = self.searchcols(image, 0, y, top, bottom, True)
        right = self.searchcols(image, y + 1, len(image[0]), top, bottom, False)
        return (bottom - top) * (right - left)

    def searchrows(self, image, i, j, option):

        while i < j:
            m = i + (j - i) / 2
            if ('1' in image[m]) == option:
                j = m
            else:
                i = m + 1
        return i

    def searchcols(self, image, i, j, top, bottom, option):

        while i < j:
            m = i + (j - i) / 2
            if any(image[k][m] == '1' for k in xrange(top, bottom)) == option:
                j = m
            else:
                i = m + 1
        return i