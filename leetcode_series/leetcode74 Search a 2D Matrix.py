# practice more about the fucking binary search!
class Solution(object):
    def searchMatrix(self, matrix, target):

        def binarysearch(lst, target):
            l, r = 0, len(lst)-1
            while l<r:
                mid = (l+r)/2
                if lst[mid] == target:
                    return True
                elif lst[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                if l == r:
                    if lst[r] == target:
                        return True
            if lst[0] == target or lst[-1] == target:
                return True
            else:
                return False

        i = 0
        while i<len(matrix):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0]<target:
                i += 1
                if i == len(matrix):
                    return binarysearch(matrix[i-1],target)
            else:
                if i == 0:
                    return False
                else:
                    return binarysearch(matrix[i-1],target)