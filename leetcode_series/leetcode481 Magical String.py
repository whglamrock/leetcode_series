
# generate the array in O(n). They is no easy math trick to do better than O(n)

class Solution(object):
    def magicalString(self, n):

        if n <= 0:
            return 0

        if n <= 3:
            return 1

        array = [0 for i in xrange(n)]
        array[0] = 1

        # if array[pointer] == 1, then the length of next claus that needs to be filled is 1;
        #   likewise for array[pointer] == 2
        pointer = 1
        # head, tail defines the start/end of the claus, so tail = head + array[pointer] - 1
        head, tail = 1, 2

        num = 2

        while tail < n:
            for i in xrange(head, tail + 1):
                array[i] = num
            if tail == n - 1:
                break    # to avoid index out of range
            pointer += 1
            head = tail + 1
            # notice that n might cut in the middle of a claus
            tail = min(head + array[pointer] - 1, n - 1)
            # a little trick to switch between 1 and 2
            num = num ^ 3

        count = 0
        for num in array:
            if num == 1: count += 1

        return count