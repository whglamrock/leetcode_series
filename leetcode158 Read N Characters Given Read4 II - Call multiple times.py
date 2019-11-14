
# for more info about the read4 API, refer to lc157

from collections import deque

# a memorize-able solution from practice

class Solution(object):

    def __init__(self):

        self.q = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        # step 1: pop out all necessary chars from q
        i = 0
        while n and self.q:
            buf[i] = self.q.popleft()
            i += 1
            n -= 1

        # step 2: read all chars to the deque
        oldn = n    # to mark how many chars we will need to pop from the q in the next step
        while n > 0:
            buf = [''] * 4
            l = read4(buf)
            if l == 0: break
            # we can safely use extend: e.g., if there only are 3 chars read, buf would be like ['a', 'b', 'c']
            self.q.extend(buf)
            n -= l

        # step 3: oldn tells us how many chars we are still in short of
        while oldn and self.q:
            buf[i] = self.q.popleft()
            i += 1
            oldn -= 1

        return i



'''
# original optimal solution from discussion:

from collections import deque

class Solution(object):
    def __init__(self):

        self.queue = deque()

    def read(self, buf, n):

        index = 0
        while True:

            cnm = [''] * 4
            l = read4(cnm)
            # if there less than four chars read, e.g., three, the
            #   cnm will be like ['a', 'b', 'c'] instead of ['a', 'b', 'c', '']
            self.queue.extend(cnm)

            currlen = min(len(self.queue), n - index)
            # because currlen always <= n - index, so after the
            #   following loop index will never exceed n
            for i in xrange(currlen):
                buf[index] = self.queue.popleft()
                index += 1

            if currlen == 0: break

        return index
'''