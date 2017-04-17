
# for more info about the read4 API, refer to lc157

from collections import deque

class Solution(object):
    def __init__(self):

        self.queue = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

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
# practice:

from collections import deque

class Solution(object):
    def __init__(self):

        self.q = deque()

    def read(self, buf, n):

        i = 0
        if self.q:
            while n and self.q:
                buf[i] = self.q.popleft()
                n -= 1
                i += 1

        while True:
            cnm = [''] * 4
            l = read4(cnm)
            for j in xrange(l):
                self.q.append(cnm[j])
            if len(self.q) >= n or l == 0:
                break

        while n and self.q:
            buf[i] = self.q.popleft()
            i += 1
            n -= 1

        return i
'''